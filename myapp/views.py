from django.shortcuts import render

def home(request):
    return render(request, "myapp/home.html")

def analyze(request):
    jtext = request.POST.get('text', '')
    original_text = jtext  # original save kar lo pehle

    punctuations = '''!()-[]{};:'"\,<>./?@#$%&*^_`'''

    # Checkboxes
    fullcaps         = request.POST.get('fullcaps', 'off')
    newlineremover   = request.POST.get('newlineremover', 'off')
    extralineremover = request.POST.get('extralineremover', 'off')
    removepunc       = request.POST.get('removepunc', 'off')
    titlecase        = request.POST.get('titlecase', 'off')
    reversetext      = request.POST.get('reversetext', 'off')
    wordcount        = request.POST.get('wordcount', 'off')
    charcount        = request.POST.get('charcount', 'off')
    sentencecount    = request.POST.get('sentencecount', 'off')

    transformed = False
    applied_operations = []  # kaunse options tick kiye the
    analysis = []

    # ── TRANSFORMATIONS ──

    if fullcaps == "on":
        jtext = jtext.upper()
        transformed = True
        applied_operations.append("Uppercase")

    if titlecase == "on":
        jtext = jtext.title()
        transformed = True
        applied_operations.append("Title Case")

    if newlineremover == "on":
        jtext = " ".join(jtext.splitlines())
        transformed = True
        applied_operations.append("Remove New Lines")

    if extralineremover == "on":
        analyzed = ""
        for index, char in enumerate(jtext):
            if index + 1 < len(jtext):
                if jtext[index] == " " and jtext[index+1] == " ":
                    pass
                else:
                    analyzed += char
            else:
                analyzed += char
        jtext = analyzed
        transformed = True
        applied_operations.append("Remove Extra Spaces")

    if removepunc == "on":
        analyzed = ""
        for char in jtext:
            if char not in punctuations:
                analyzed += char
        jtext = analyzed
        transformed = True
        applied_operations.append("Remove Punctuations")

    if reversetext == "on":
        jtext = jtext[::-1]
        transformed = True
        applied_operations.append("Reverse Text")

    # ── ANALYSIS ──

    if wordcount == "on":
        analysis.append({'label': 'Word Count', 'value': len(jtext.split())})
        applied_operations.append("Word Count")

    if charcount == "on":
        analysis.append({'label': 'Character Count', 'value': sum(1 for c in jtext if c.isalpha())})
        applied_operations.append("Character Count")

    if sentencecount == "on":
        count = jtext.count('.') + jtext.count('!') + jtext.count('?')
        analysis.append({'label': 'Sentence Count', 'value': count})
        applied_operations.append("Sentence Count")

    return render(request, "myapp/analyse.html", {
        'original_text': original_text,
        'transformed_text': jtext,
        'transformed': transformed,
        'analysis': analysis,
        'applied_operations': applied_operations,
    })

def About(request):
    return render(request, "myapp/about.html")