import tkinter as tk
from tkinter import filedialog
from ramanbiolibui.utils.search import spectra_slk_search, spectra_pm_search

class JSHandler:
    def __init__(self, browser):
        self.result_df = None
        self.browser = browser

    def slk_search(self, spectra, filename, window_size, table_n, plot_n):
        try:
            self.result_df, result_html = spectra_slk_search(spectra, filename, int(window_size), int(table_n), int(plot_n))
            self.browser.ExecuteFunction("updateResult", result_html)
        except Exception as e:
            self.browser.ExecuteFunction("updateResult", f"""<div class="error results">
            <h2>Error</h2>
            <span>Error when searching: {e}</span>
        </div>""")

    def pm_search(self, source_type, sort_col, tolerance, penalty, results_n, plot_n, input_dict):
        try:
            self.result_df, result_html = spectra_pm_search(
                source_type, sort_col, int(tolerance), penalty, int(results_n), int(plot_n), input_dict
            )
            self.browser.ExecuteFunction("updateResult", result_html)
        except Exception as e:
            print(e)
            self.browser.ExecuteFunction("updateResult", f"""<div class="error results">
            <h2>Error</h2>
            <span>Error when searching: {e}</span>
        </div>""")

    def save_csv(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv", 
            filetypes=[("CSV files", "*.csv"), ("All Files", "*.*")],
            title="Save CSV File"
        )
        if file_path and self.result_df is not None:
            self.result_df.to_csv(file_path, index=False)
            print(f"CSV saved at: {file_path}")
        else:
            print("Save cancelled or no results available")
