import re
phoneNumberRegex = re.compile(r'')
mo = phoneNumberRegex.findall('''{
  "name": "sagar-aio-bot",
  "description": "All in one bot for torrenting",
  "repository": "https://github.com/dark-phoenix-op/aio-bot/",
  "keywords": ["node", "express", "bot", "torrent", "automation"],
  "builpacks": [
    { "url": "heroku/nodejs" },
    { "url": "https://github.com/jontewks/puppeteer-heroku-buildpack.git" }
  ]
}''')
print(mo)