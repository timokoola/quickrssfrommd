import datetime
import os

feed_meta = f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Timo Koola&#39;s word blog </title>
  <subtitle>Just a RSS Feed of Finnish words</subtitle>
  <link href="https://timokoola.github.io/quickrssfrommd/feed/feed.xml" rel="self"/>
  <link href="https://timokoola.github.io/quickrssfrommd/"/>
  <updated>{datetime.datetime.utcnow().isoformat()}</updated>
  <id>https://timokoola.github.io/quickrssfrommd/</id>
  <author>
    <name>Timo Koola</name>
    <email>timo@timokoola.com</email>
  </author>
"""

feed_closing = """
</feed>
"""


def generate_feed_item(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    # get the file modified timestamp from file system
    filedate = datetime.datetime.fromtimestamp(os.path.getmtime(filename)).isoformat()

    summary = lines[0].strip()
    full_text = "\n".join(lines)
    title = f"Words from {filedate}"

    link = f"https://timokoola.github.io/quickrssfrommd/{filename}"

    return f"""<entry>
    <title>{title}</title>
    <link href="{link}"/>
    <summary>{summary}</summary>
    <updated>{filedate}</updated>
    <content type="text">{full_text}</content>
    <id>{link}</id>
  </entry>
  """


if __name__ == "__main__":
    # list files in markdown folder, include the folder name in the path
    files = [f"markdown/{f}" for f in os.listdir("markdown")]

    entries = [generate_feed_item(f) for f in files]

    with open("feed.xml", "w") as f:
        f.write(feed_meta)
        for entry in entries:
            f.write(entry)
        f.write(feed_closing)
