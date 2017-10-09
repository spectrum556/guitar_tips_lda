from web_application.app import db

class SongVersions(db.Model):
    __tablename__ = 'song_versions'

    id = db.Column(db.BigInteger, primary_key=True)
    song_id = db.Column(db.BigInteger, db.ForeignKey('song.id'))
    text = db.Column(db.String())
    comment = db.Column(db.String())
    created_at = db.Column(db.BigInteger)
    updated_at = db.Column(db.BigInteger)

    def __init__(self, song_id, text, comment, created_at, updated_at):
        self.song_id = song_id
        self.text = text
        self.comment = comment
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<song_version id = {}, song_id = {}>'.format(self.id, self.song_id)


if __name__ == '__main__':
    song = SongVersions.query.filter_by(id=1)
    print(song.text)
