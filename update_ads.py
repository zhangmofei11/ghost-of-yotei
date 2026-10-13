import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/b7f564fd90f291f3205f6fab9a828d6e"></script>
<script data-cfasync="false" src="https://bauval.org/14/ae8db81b158b1e0c39cfd53f4d337fca"></script>
<script>
  atOptions = {
    'key' : 'd9b23650876a001af99c4015c3fcf594',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/d9b23650876a001af99c4015c3fcf594"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-b7f564fd90f291f3205f6fab9a828d6e"></div>
</div>'''

files = ['index.html', 'walkthrough.html', 'characters.html', 'weapons.html', 'collectibles.html', 'tips.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if 'd9b23650876a001af99c4015c3fcf594' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-b7f564fd90f291f3205f6fab9a828d6e' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')