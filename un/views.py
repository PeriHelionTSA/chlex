def index(request):
    from django.http import HttpResponse
    return HttpResponse("<head><title>Das ist noch ein Test</title> </head> <body><h1>Title</h1><div style=\"background-color: yellow;\">das ist ein Test</div><h2>Subtitle</h2><p><a href=\"admin\">das</a> ist ein <span style=\"background-color: green;\">test</span></p> </body>")
