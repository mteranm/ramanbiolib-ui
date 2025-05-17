import numpy as np
import pandas as pd
from scipy import interpolate
from scipy.signal import find_peaks
from io import StringIO
from ramanbiolibui.utils.files import get_resource_path
from ramanbiolib.search import PeakMatchingSearch, SpectraSimilaritySearch

def format_df_result(result_df):
    result_df['laser'] = result_df['laser'].astype(float)
    result_df = result_df.set_index(result_df.index.to_numpy()+1)
    return result_df

def format_result_html(table, full_table, plot):
    # Read results HTML
    with open(get_resource_path("ramanbiolibui/templates/results.html"), "r", encoding="utf-8") as file:
        results_html = file.read()
    return results_html.format(
        table=table,
        full_table=full_table,
        plot=plot
    )

def load_wire_txt(csv_data):
    spectra_df = (
        pd.read_csv(StringIO(csv_data), delimiter="\t", header=0, names=['wavenumbers', 'intensity', 'empty'])
        .drop("empty", axis=1)
        .sort_values("wavenumbers")
    )
    return np.array(spectra_df['wavenumbers']), np.array(spectra_df['intensity'])

def load_csv(csv_data):
    spectra_df = (
        pd.read_csv(StringIO(csv_data), delimiter=",", header=0, names=['wavenumbers', 'intensity'])
        .sort_values("wavenumbers")
    )
    return np.array(spectra_df['wavenumbers']), np.array(spectra_df['intensity'])

def load_spectrum(csv_data, filename):
    x, y = load_wire_txt(csv_data) if ".txt" in filename else load_csv(csv_data)
    f = interpolate.interp1d(x, y)
    wavenumbers = np.arange(max(int(np.ceil(x.min())), 450), min(int(x.max()), 1800) + 1)
    if len(wavenumbers) == 0:
        raise Exception("The spectrum does not contain any wavenumber in the range 450-1800")
    y = f(wavenumbers)
    y = (y - np.min(y)) / (np.max(y) - np.min(y))
    return y, wavenumbers

def spectra_slk_search(csv_data, filename, w, results_n, plot_n):
    w = int(w)
    results_n = int(results_n)
    plot_n = int(plot_n)
    y, wavenumbers = load_spectrum(csv_data, filename)
    spectra_search = SpectraSimilaritySearch(wavenumbers=wavenumbers)
    search_results_obj = (
        spectra_search.search(y, 
            similarity_method='slk',
            similarity_params=w
        )
    )
    search_results = (
        search_results_obj.get_results().reset_index(drop=True)
        .rename({"similarity_score": "slk_score"}, axis=1)
        [['type', 'id', 'component', 'laser', 'reference', 'slk_score']]
    )
    return format_df_result(search_results), format_result_html(
        format_df_result(search_results[:results_n]).to_html(render_links=True), 
        format_df_result(search_results).to_html(render_links=True), 
        search_results_obj.plot_results(n=plot_n).to_html(full_html=False)
    )

def get_peaks(source_type, input_dict):
    if source_type == "peaks":
        peaks_wavenumbers = [int(v) for v in input_dict['peaks'].split(",") if int(v) >= 450 and int(v) <=1800]
        wavenumbers = np.arange(450, 1801)
        peaks = np.searchsorted(wavenumbers, peaks_wavenumbers)
        return peaks, [], wavenumbers
    y, wavenumbers = load_spectrum(input_dict['csv_data'], input_dict['filename'])
    peaks, _ = find_peaks(y, prominence=float(input_dict['prominence']))
    return peaks, y, wavenumbers

def spectra_pm_search(source_type, sort_col, tolerance, penalty, results_n, plot_n, input_dict):
    results_n = int(results_n)
    plot_n = int(plot_n)
    penalty = penalty
    tolerance = int(tolerance)
    sort_col = sort_col

    peaks, y, wavenumbers = get_peaks(source_type, input_dict)
    print(f"Number of peaks: {len(peaks)}")
    if len(peaks) > 100:
        raise Exception("The selected configuration extracts too many peaks from the specturm. Increase the prominence threshold.")
    elif len(peaks) == 0:
        raise Exception("No peaks detected. Decrease the prominence threshold")

    spectra_search = SpectraSimilaritySearch(wavenumbers=wavenumbers)
    peaks_search = PeakMatchingSearch(wavenumbers)

    search_results_obj = (
        peaks_search.search(
            wavenumbers[peaks],
            tolerance=tolerance,
            tol_penalty=penalty,
        )
    )
    search_results = (
        search_results_obj.get_results(sort_col=sort_col)
        [['type', 'id', 'component', 'laser', 'reference', 
          'MR', 'RMR', 'IUR', 'PIUR']]
        .reset_index(drop=True)
    )
    return format_df_result(search_results), format_result_html(
        format_df_result(search_results[:results_n]).to_html(render_links=True), 
        format_df_result(search_results).to_html(render_links=True), 
        search_results_obj.plot_results(n=plot_n, query_spectrum=y, sort_col=sort_col).to_html(full_html=False)
    )