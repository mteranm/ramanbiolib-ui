from cefpython3 import cefpython as cef
from handlers.jshandler import JSHandler
from handlers.linkhandler import ExternalLinkHandler
from utils.files import get_resource_path, image_to_base64

def main():
    cef.Initialize()

    # Read index HTML
    with open(get_resource_path("src/templates/index.html"), "r", encoding="utf-8") as file:
        html_content = file.read()

    # Read styles
    with open(get_resource_path("src/static/styles.css"), "r", encoding="utf-8") as file:
        styles = file.read()

    # Read scripts
    with open(get_resource_path("src/static/scripts.js"), "r", encoding="utf-8") as file:
        scripts = file.read()

    # Read JQuery
    with open(get_resource_path("src/static/jquery.min.js.js"), "r", encoding="utf-8") as file:
        jq_scripts = file.read()

    # Read search box HTML
    with open(get_resource_path("src/templates/search.html"), "r", encoding="utf-8") as file:
        search_box_html = file.read()

    html_content = html_content.format(
        jquery_script=jq_scripts,
        styles=styles, scripts=scripts, 
        logo_img=image_to_base64(get_resource_path("src/img/logo.png")),
        content=search_box_html,
        uoc_img=image_to_base64(get_resource_path("src/img/uoc.png")),
        icfo_img=image_to_base64(get_resource_path("src/img/icfo.png")),
    )

    window_info = cef.WindowInfo()
    window_info.SetAsChild(0)
    window_info.windowRect = [100, 100, 1400, 1100]

    global browser
    browser = cef.CreateBrowserSync(
        window_info=window_info,
        url="data:text/html," + html_content,
        window_title="Raman Spectral Search in Biomolecules Database"
    )

    # Extrenal links handler
    browser.SetClientHandler(ExternalLinkHandler())

    # Bind JavaScript functions to Python
    js_handler = JSHandler(browser)
    bindings = cef.JavascriptBindings()
    bindings.SetObject("pyHandler", js_handler)
    browser.SetJavascriptBindings(bindings)

    cef.MessageLoop()
    cef.Shutdown()


if __name__ == "__main__":
    main()
