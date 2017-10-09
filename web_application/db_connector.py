from web_application.model import SongVersions
from pprint import pprint

class Connector:

    def get_text(self, id):
        return SongVersions.query.filter_by(id=id).first().text

    def get_all_texts(self):
        texts = []
        for version in SongVersions.query.yield_per(20):
            texts.append((version.song_id, version.text))

        return sorted(texts, key=lambda item: item[0])

# TODO: fix id - 1 and convert to list
# TODO: look about warning

if __name__ == '__main__':
    con = Connector()
    print(con.get_text(0))
    pprint(con.get_all_texts()[:10])
