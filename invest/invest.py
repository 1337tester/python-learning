from currency_viewer import currency_viewer as cv

a = cv.CurrencyViewer()
a.processCViewer(log=True, currency="EUR", time="rfc1123")
a.display_results()
