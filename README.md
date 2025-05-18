<picture align="center">
  <img alt="RamanBiolib logo" style="background:white; padding: 20px;" src="https://raw.githubusercontent.com/mteranm/ramanbiolib-ui/main/ramanbiolibui/img/logo.png">
</picture>

# RamanBiolib UI:  

A standalone UI for Biomolecule Identifiaction by means of Raman Spectroscopy using [RamanBiolib](https://github.com/mteranm/ramanbiolib)

## Getting started

### Python package

Installation:


```
pip install ramanbiolib-ui
```

Run:

```
ramanbiolib-ui
```

### Windows executable file

You can download the Windows executable (`.exe` file) from the **Releases** section of this repository:

1. Go to the [Releases page](https://github.com/mteranm/ramanbiolib-ui/releases).
2. Find the latest release (or the version you want).
3. Under the **Assets** section, click on the `ramanbiolib-ui.exe` file to download it.
4. Run the downloaded file to start the application.

> **Note**: This executable file is self-signed, so Windows and/or antivirus software may flag it as potentially unsafe. However, the file is secure — it is simply a packaged version of this open-source code created using PyInstaller. If you have any concerns about running the executable, you can always install and run the Python version instead.

## How to use this tool

### Spectral Linear Kernel (SLK) similarity search

This uses the full spectra plot to rank the database components by its SLK similarity to the unknown specturm.

Parameters:
- **Raman spectrum file**: the unnknown spectrum file containing the wavenumbers and intensity.
- **Window size**: the value of the window (W) parameter in SLK.
- **Top N table**: the number of components to show in the result table.
- **Top N plot**: the number of components to show in the result plot.


![SLK search](https://raw.githubusercontent.com/mteranm/ramanbiolib-ui/main/docs/slk_search.png)

The search results display the ranked table of the most similar biomolecules in the RamanBiolib database:

![SLK table](https://raw.githubusercontent.com/mteranm/ramanbiolib-ui/main/docs/slk_table.png)


and the spectra comparison plot:

![SLK plot](https://raw.githubusercontent.com/mteranm/ramanbiolib-ui/main/docs/slk_plot.png)


### Peak matching search

This matching calculate the matching between the specturm extracted peak positions and each database component peak positions.

Parameters:

- **Source:**
    - **spectrum**: the source is a spectrum file (as in SLK similarity search)
        - **Raman spectrum file**: the unnknown spectrum file containing the wavenumbers and intensity.
        - **Peak detection prominence**: the min prominence threshold for peak detection of the uploaded spectrum once the specturm is min-max normalized. The peak detection is done using scipy find_peaks function.
    - **peaks list**: 
        - **Peaks wavenumbers**: the source is a comma-separated list of peaks wavenumbers positions (cm⁻¹). Example: 100,500,652,1205,1652 (step=1cm⁻¹, min=450, max=1800)
- **Tolerance size**: the simmetrical maximum distance tolerance for peak matching.
- **Penalty type**: the penalty function for PIUR calculation. Linear or Inverse power (1/x).
- **Sorted by**: the metric used to sort the results (IUR, MR, RMR, PIUR). Default IUR. 
  - Considering query spectrum peaks Pa and DB spectrum peaks Pb: 
    - MR (Matching Ratio) = intersection(Pa, Pb)/len(Pa) 
    - RMR (Reverse Matching Ratio) = intersection(Pa, Pb)/len(Pb) 
    - IUR (Intersection Union Ratio) = intersection(Pa, Pb)/union(Pa, Pb) 
    - PIUR (Penalized Intersection Union Ratio) = penalized_intersection(Pa, Pb)/union(Pa, Pb) 
- **Top N table**: the number of components to show in the result table.
- **Top N plot**: the number of components to show in the result plot.


![PM search](https://raw.githubusercontent.com/mteranm/ramanbiolib-ui/main/docs/pm_search.png)

The search results display the ranked table of the most similar biomolecules in the RamanBiolib database:

![PM table](https://raw.githubusercontent.com/mteranm/ramanbiolib-ui/main/docs/pm_table.png)


and the spectra comparison plot:

![PM plot](https://raw.githubusercontent.com/mteranm/ramanbiolib-ui/main/docs/pm_plot.png)


## How to cite this tool

If you use this tool for research, please cite us:

> Terán, M and Ruiz, JJ and Loza-Álvarez, P and Masip, D and Merino, D, *Open Raman Spectral Library for Biomolecule Identification*. Available at SSRN: https://ssrn.com/abstract=5185686 or http://dx.doi.org/10.2139/ssrn.5185686 

## License

[GNU GPL v3](https://raw.githubusercontent.com/mteranm/ramanbiolib-ui/main/LICENSE)