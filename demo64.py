import wikipedia

print wikipedia.summary("Elephant")
print wikipedia.summary("Lion")
print wikipedia.search("C++")
taipei = wikipedia.page("Taiwan")
print taipei.url, taipei.title
#print taipei.links[:2]
for link in taipei.links[:5]:
    print link
print taipei.content
wikipedia.set_lang("zh")
print wikipedia.summary("Thor", sentences=3)