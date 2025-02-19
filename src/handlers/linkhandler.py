import webbrowser

class ExternalLinkHandler:
    def OnBeforeBrowse(self, browser, frame, request, is_redirect, user_gesture):
        url = request.GetUrl()
        if url.startswith("http"):  # If it's not a local file, open externally
            webbrowser.open(url)  # Open in the default system browser
            return True  # Cancel the default behavior in CEF
        return False  # Continue normal browsing for internal links

    def OnBeforePopup(self, *args, **kwargs):
        target_url = kwargs['target_url']
        # Prevent blank new CEF window from opening
        if target_url.startswith("http"):
            webbrowser.open(target_url)  # Open in external browser
            return True  # Block popup in CEF
        return False  # Allow normal popups if needed