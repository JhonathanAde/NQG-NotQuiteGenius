from app.models import db, Annotation

def seed_annotations():

    objects = [
      Annotation(
        user_id=1,
        song_id=1,
        lyric_key="I never would've known",
        content="First annotation for song 1"
      ),
      Annotation(
        user_id=1,
        song_id=1,
        lyric_key="Like you were a trophy or a champion ring<br />And there was one prize I'd cheat to win",
        content="Second annotation for song 1 spans a 'br' tag"
      ),
      Annotation(
        user_id=2,
        song_id=1,
        lyric_key="I'm begging for you to take my hand",
        content="Third annotation for song 1 is found in multiple places in the text"
      ),
      Annotation(
        user_id=1,
        song_id=2,
        lyric_key="Yeah, and she screamin', \"She knows this\"",
        content="First annotation for song 2 has nested quotation marks"
      ),
      Annotation(
        user_id=2,
        song_id=2,
        lyric_key="let me set it off",
        content="Second annotation for song 2"
      ),
      Annotation(
        user_id=2,
        song_id=2,
        lyric_key="Someone say they saw that man, ayy<br />And they say, \"No, ain't no controllin' him,\" ayy<br />Yeah, it's a myth, up in this bitch, no takin' flicks<br />Climbed out the treacherous bottomless pit<br />Yeah, I'm reborn and my life is the shit, heaven (Go)<br />",
        content="Third annotation for song 2 spans four 'br' tags"
      ),
    ]

    db.session.bulk_save_objects(objects)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_annotations():
    db.session.execute('TRUNCATE annotations;')
    db.session.commit()
