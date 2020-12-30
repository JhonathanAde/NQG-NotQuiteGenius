from app.models import db, Song

def stripNewLines(song):
    song.lyrics = song.lyrics.replace('\n', '')
    song.lyrics = song.lyrics.replace('\t', '')
    return song

def seed_songs():
    objects = [
        Song(
        title = 'Willow',
        artist_id = 1,
        lyrics = """[Verse 1]<br />
I'm like the water when your ship rolled in that night<br />
Rough on the surface, but you cut through like a knife<br />
And if it was an open-shut case<br />
I never would've known from that look on your face<br />
Lost in your current like a priceless wine<br />
<br />
[Chorus]<br />
The more that you say, the less I know<br />
Wherever you stray, I follow<br />
I'm begging for you to take my hand<br />
Wreck my plans, that's my man<br />
<br />
[Verse 2]<br />
Life was a willow and it bent right to your wind<br />
Head on the pillow, I could feel you sneakin' in<br />
As if you were a mythical thing<br />
Like you were a trophy or a champion ring<br />
And there was one prize I'd cheat to win<br />
<br />
[Chorus]<br />
The more that you say, the less I know<br />
Wherever you stray, I follow<br />
I'm begging for you to take my hand<br />
Wreck my plans, that's my man<br />
You know that my train could take you home<br />
Anywhere else is hollow<br />
I'm begging for you to take my hand<br />
Wreck my plans, that's my man<br />
<br />
[Bridge]<br />
Life was a willow and it bent right to your wind<br />
They count me out time and time again<br />
Life was a willow and it bent right to your wind<br />
But I come back stronger than a '90s trend<br />
<br />
[Verse 3]<br />
Wait for the signal, and I'll meet you after dark<br />
Show me the places where the others gave you scars<br />
Now this is an open-shut case<br />
I guess I should've known from the look on your face<br />
Every bait-and-switch was a work of art<br />
<br />
[Chorus]<br />
The more that you say, the less I know<br />
Wherever you stray, I follow<br />
I'm begging for you to take my hand<br />
Wreck my plans, that's my man<br />
You know that my train could take you home<br />
Anywhere else is hollow<br />
I'm begging for you to take my hand<br />
Wreck my plans, that's my man<br />
The more that you say, the less I know<br />
Wherever you stray, I follow<br />
I'm begging for you to take my hand<br />
Wreck my plans, that's my man<br />
You know that my train could take you home<br />
Anywhere else is hollow<br />
I'm begging for you to take my hand<br />
Wreck my plans, that's my man<br />
<br />
[Outro]<br />
Hey, that's my man<br />
That's my man<br />
Yeah, that's my man<br />
Every bait-and-switch was a work of art<br />
That's my man<br />
Hey, that's my man<br />
I'm begging for you to take my hand<br />
Wreck my plans, that's my man"""
        ),
        Song(
        title = 'She Knows This',
        artist_id = 2,
        lyrics = """[Intro: Mark Webber & Michael Cera]<br />
Scott, let it go<br />
Don't give 'em the satisfaction<br />
What if I want the satisfaction?<br />
<br />
[Chorus]<br />
Mm-mm-mm<br />
Yeah, and she see me, she knows this<br />
Mm-mm-mm<br />
Yeah, and she screamin', "She knows this"<br />
Mm-mm-mm<br />
Yeah, and she see me, she knows this<br />
Yeah, hmm<br />
Mm-mm-mm<br />
Yeah, and she see me, she knows this<br />
Mm-mm-mm<br />
Yeah, and she screamin', "She knows this"<br />
Mm-mm-mm<br />
Yeah, and she see me, she knows this<br />
Yeah, hmm-hmm<br />
<br />
[Verse 1]
Here we go, step in (Yeah, yeah) and we gon' tear shit up (Uh)<br />
Yeah, they got double cups, but me and my boo got two fat blunts (Yeah)<br />
Roll it up (Gang), ooh, talk about dude, I give two fucks (Fuck)<br />
But we know (Ooh), truth, duck all the ho shit, burnin' the burnt clips (Nah)<br />
Now listen, wow, baby, let me set it off<br />
In your itty-bitty 'kini, such a vision, oh<br />
You my fix, you's a hit in forever long<br />
Workin' it, your sweaty body, love to see it go, ooh-ooh<br />
Take a ride if you like, let's see<br />
Do whatever you like and we (Yeah)<br />
On a mission tonight, ooh-ooh<br />
Live a hell of a life (Yeah)<br />
Someone say they saw that man, ayy<br />
And they say, "No, ain't no controllin' him," ayy<br />
Yeah, it's a myth, up in this bitch, no takin' flicks<br />
Climbed out the treacherous bottomless pit<br />
Yeah, I'm reborn and my life is the shit, heaven (Go)<br />
<br />
[Chorus]<br />
Mm-mm-mm<br />
Yeah, and she see me, she knows this<br />
Mm-mm-mm<br />
Yeah, and she screamin', "She knows this"<br />
Mm-mm-mm<br />
Yeah, and she see me, she knows this<br />
Yeah, hmm<br />
Mm-mm-mm<br />
Yeah, and she see me, she knows this<br />
Mm-mm-mm<br />
Yeah, and she screamin', "She knows this"<br />
Mm-mm-mm<br />
Yeah, and she see me, she knows this<br />
Yeah, hmm-hmm<br />
<br />
[Verse 2]<br />
Yeah, gangs of women givin' lovin', easy sinnin'<br />
Suppose you got two hoes that go both ways, don't know my limit<br />
Know what it is, fall into the void, this how I'm livin'<br />
Can't ask for better options, it's the captain of the ship isn't it?<br />
Yeah, yo, this for my sanity<br />
Some play some days into the night<br />
I say you can't judge me, babe, I'm twisted in the brain, know why (Yeah)<br />
See I can't be stressin' (No, no, I can't stress)<br />
I just need my medicine (Yeah baby, I need it)<br />
Baby, come and learn these lessons (Come, baby, and see)<br />
Been around and around again (Boom-boom, boom-boom)<br />
Cuttin' loose with the troops and, no, we ain't lie<br />
This the move, come and tell your group get inside the groove<br />
We at the trippy house, show me how you do<br />
Live a hell of a life<br />
<br />
[Chorus]<br />
Mm-mm-mm<br />
Yeah, and she see me, she knows this<br />
Mm-mm-mm<br />
Yeah, and she screamin', "She knows this"<br />
Mm-mm-mm<br />
Yeah, and she see me, she knows this<br />
Yeah, hmm<br />
Mm-mm-mm<br />
Yeah, and she see me, she knows this<br />
Mm-mm-mm<br />
Yeah, and she screamin', "She knows this"<br />
Mm-mm-mm<br />
Yeah, and she see me, she knows this<br />
Yeah, hmm-hmm<br />
<br />
[Outro]<br />
Yeah, yeah<br />
Gettin', Gettin', Gettin'<br />
Crazy<br />
Hmm, hmm, hmm-hmm"""
        ),
        Song(
        title = 'Reborn',
        artist_id = 2,
        lyrics = """[Intro: Kid Cudi]<br />
Hmm, I'm wide awake, I'm wide awake<br />
I'm wide awake<br />
Hey, I'm wide awake, I'm wide awake<br />
I'm wide awake<br />
<br />
[Chorus: Kid Cudi]<br />
I'm so—I'm so reborn, I'm movin' forward<br />
Keep movin' forward, keep movin' forward<br />
Ain't no stress on me Lord, I'm movin' forward<br />
Keep movin' forward, keep movin' forward<br />
I'm so—I'm so reborn, I'm movin' forward<br />
Keep movin' forward, keep movin' forward<br />
Ain't no stress on me Lord, I'm movin' forward<br />
Keep movin' forward, keep movin' forward<br />
<br />
[Bridge: Kid Cudi]<br />
Hmm, I'm wide awake, I'm wide awake<br />
I'm wide awake<br />
Hey, I'm wide awake, I'm wide awake<br />
I'm wide awake<br />
<br />
[Verse 1: Kanye West]<br />
Very rarely do you catch me out<br />
Y'all done "specially invited guest"'d me out<br />
Y'all been tellin' jokes that's gon' stress me out<br />
Soon as I walk in, I'm like, "Let's be out"<br />
I was off the chain, I was often drained<br />
I was off the meds, I was called insane<br />
What a awesome thing, engulfed in shame<br />
I want all the rain, I want all the pain<br />
I want all the smoke, I want all the blame<br />
Cardio audio, let me jog your brain<br />
Caught in the Audy Home, we was all detained<br />
All of you Mario, it's all a game<br />
<br />
[Chorus: Kid Cudi]<br />
I'm so—I'm so reborn, I'm movin' forward<br />
Keep movin' forward, keep movin' forward<br />
Ain't no stress on me Lord, I'm movin' forward<br />
Keep movin' forward, keep movin' forward<br />
I'm so—I'm so reborn, I'm movin' forward<br />
Keep movin' forward, keep movin' forward<br />
Ain't no stress on me Lord, I'm movin' forward<br />
Keep movin' forward, keep movin' forward<br />
<br />
[Verse 2: Kid Cudi]<br />
I had my issues, ain't that much I could do<br />
Peace is somethin' that starts with me (with me)<br />
At times, wonder my purpose<br />
Easy than to feel worthless<br />
But, peace is somethin' that starts with me (with me, with me)<br />
Had so much on my mind, I didn't know where to go<br />
I've come a long way from them hauntin' me<br />
Had me feelin' oh so low<br />
Ain't no stoppin' you, no way<br />
Oh, things ain't like before<br />
Ain't no stoppin' you, no way<br />
No stress yes, I'm so blessed and-<br />
<br />
[Chorus: Kid Cudi]
I'm so—I'm so reborn, I'm movin' forward<br />
Keep movin' forward, keep movin' forward<br />
Ain't no stress on me Lord, I'm movin' forward<br />
Keep movin' forward, keep movin' forward<br />
I'm so—I'm so reborn, I'm movin' forward<br />
Keep movin' forward, keep movin' forward<br />
Ain't no stress on me Lord, I'm movin' forward<br />
Keep movin' forward, keep movin' forward<br />
<br />
[Bridge: Kid Cudi]<br />
(Movin' forward, movin' forward, movin' forward)<br />
Movin' forward, keep movin' forward<br />
Something was wrong (Keep movin' forward)<br />
Couldn't hold on, why? (Keep movin' forward)<br />
So long (Keep movin' forward)<br />
Sit here in this storm (Keep movin' forward)<br />
Time goes on (Keep movin' forward)<br />
Really couldn't find my way out (Keep movin' forward)<br />
Of the storm (Keep movin' forward)<br />
Which way do I go?
<br />
[Chorus: Kid Cudi]<br />
I'm so—I'm so reborn, I'm movin' forward (which way do I go?)<br />
Keep movin' forward, keep movin' forward (which way do I go?)<br />
Ain't no stress on me Lord, I'm movin' forward (which way do I go?)<br />
Keep movin' forward, keep movin' forward<br />
Keep movin' forward, keep movin' forward<br />
Keep movin' forward, keep movin' forward<br />
Keep movin' forward, keep movin' forward<br />
Keep movin' forward, keep movin' forward<br />
I'm so—I'm so reborn, I'm movin' forward<br />
Keep movin' forward, keep movin' forward<br />
Ain't no stress on me Lord, I'm movin' forward<br />
Keep movin' forward, keep movin' forward"""
        ),
        Song(
        title = 'Tequila Shots',
        artist_id = 2,
        lyrics = """[Intro]<br />
Duh-duh-duh, duh, duh, duh<br />
As he falls back deeper, into a state<br />
The return (Dot Da Genius, baby)<br />
(Daytrip took it to ten, hey)<br />
<br />
[Verse 1]<br />
Nights my mind is speedin' by, I'm holdin' on<br />
Askin' God to help 'em, are you hearin' me?<br />
Girl is tellin' me she don't know what she want<br />
Lotta demons creepin' up, they're livin' underneath<br />
Gotta take a minute, y'all, traveled far<br />
Feelin' somethin', no, I can't ignore my instincts<br />
Back just where I started, it's the same old damaged song<br />
It's the shit I need
<br />
[Pre-Chorus]<br />
Tryna find it on the right track<br />
Oh, wanna be just where the free at<br />
Hm, talk to Him, He don't speak back<br />
Hm, can't lose, I'm in the third act<br />
Lord seein' me swerve<br />
Do this to my loved ones, I've got some nerve<br />
Don't think I'm not sorry<br />
<br />
[Chorus]<br />
Hm, hear me now, hey<br />
This time I'm ready for it<br />
Can't stop this war in me<br />
Can't stop this war in me, in me, in me<br />
Hm, hear me now, hey<br />
This time I'm ready for it<br />
This fight, this war in me<br />
This fight, this war in me, in me, in me<br />
<br />
[Post-Chorus]<br />
Hm, I been here before<br />
Hm, hm, I been here before, hm<br />
Can't stop this war in me<br />
Can't stop this war in me, in me, in me<br />
As the story goes, hey, hey<br />
As the story goes, hm<br />
This fight, this war in me<br />
This fight, this war in me, in me, in me<br />
<br />
[Verse 2]<br />
(Yeah) Standin' on the cliff right off Mulholland Drive<br />
(Yeah) Back up on my late night session remedy<br />
(Oh) Something 'bout the night that keep me safe and warm<br />
Just me, the universe, and everything I think<br />
Lotta shit is weighin' on me, it's a storm<br />
Never thought I would be back here bleeding<br />
I'm not just some sad dude<br />
You can see my life, how I grew, I want serenity<br />
<br />
[Pre-Chorus]<br />
Tryna find it on the right track<br />
Oh, wanna be just where the free at<br />
Talk to Him, He don't speak back<br />
Hm, can't lose, I'm in the third act<br />
See, it seems I'll never learn<br />
I won't stop 'til I crash and burn<br />
Tell my mom I'm sorry<br />
<br />
[Chorus]<br />
Hm, hear me now, hey<br />
This time I'm ready for it<br />
Can't stop this war in me<br />
Can't stop this war in me, in me, in me<br />
Hm, hear me now, hey<br />
This time I'm ready for it<br />
This fight, this war in me<br />
This fight, this war in me, in me, in me<br />
<br />
[Post-Chorus]<br />
I been here before, hey, hey<br />
I been here before, hm<br />
Can't stop this war in me<br />
Can't stop this war in me, in me, in me<br />
And the story goes, hey, hey<br />
As the story goes, hm<br />
This fight, this war in me<br />
This fight, this war in me, in me, in me"""
        ),
        Song(
        title = 'Blinding Lights',
        artist_id = 3,
        lyrics = """[Intro]<br />
Yeah<br />
<br />
[Verse 1]<br />
I've been tryna call<br />
I've been on my own for long enough<br />
Maybe you can show me how to love, maybe<br />
I'm going through withdrawals<br />
You don't even have to do too much<br />
You can turn me on with just a touch, baby<br />
<br />
[Pre-Chorus]<br />
I look around and<br />
Sin City's cold and empty (Oh)<br />
No one's around to judge me (Oh)<br />
I can't see clearly when you're gone<br />
<br />
[Chorus]<br />
I said, ooh, I'm blinded by the lights<br />
No, I can't sleep until I feel your touch<br />
I said, ooh, I'm drowning in the night<br />
Oh, when I'm like this, you're the one I trust<br />
Hey, hey, hey<br />
<br />
[Verse 2]<br />
I'm running out of time<br />
'Cause I can see the sun light up the sky<br />
So I hit the road in overdrive, baby, oh<br />
<br />
[Pre-Chorus]<br />
The city's cold and empty (Oh)<br />
No one's around to judge me (Oh)<br />
I can't see clearly when you're gone<br />
<br />
[Chorus]<br />
I said, ooh, I'm blinded by the lights<br />
No, I can't sleep until I feel your touch<br />
I said, ooh, I'm drowning in the night<br />
Oh, when I'm like this, you're the one I trust<br />
<br />
[Bridge]<br />
I'm just calling back to let you know (Back to let you know)<br />
I could never say it on the phone (Say it on the phone)<br />
Will never let you go this time (Ooh)<br />
<br />
[Chorus]<br />
I said, ooh, I'm blinded by the lights<br />
No, I can't sleep until I feel your touch<br />
Hey, hey, hey<br />
Hey, hey, hey<br />
<br />
[Outro]<br />
I said, ooh, I'm blinded by the lights<br />
No, I can't sleep until I feel your touch"""
        ),
    ]

    objects = [stripNewLines(song) for song in objects]
    db.session.bulk_save_objects(objects)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_songs():
    db.session.execute('TRUNCATE songs;')
    db.session.commit()
