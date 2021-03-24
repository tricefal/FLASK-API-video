from main import db




class Video_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, default=1)
    likes = db.Column(db.Integer, default=1)

    def __repr__(self):
        return f"Video : (title={self.title}, views={self.views}, likes={self.likes})"

# db.create_all()
