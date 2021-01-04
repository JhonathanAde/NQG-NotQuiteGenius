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
        image = 'https://nqg-images.s3.amazonaws.com/Evermore-01.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Taylor_Swift_willow_preview.mp3',
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
        image = 'https://nqg-images.s3.amazonaws.com/Man_On_The_Moon_III-01.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Kid_Cudi_She_Knows_This.mp3',
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
        image = 'https://nqg-images.s3.amazonaws.com/kid_sees_ghosts-01.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Kid+Cudi_Reborn_Kids_See_Ghosts_preview.mp3',
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
        image = 'https://nqg-images.s3.amazonaws.com/Man_On_The_Moon_III-01.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Kid_Cudi_Tequila_Shots_preview.mp3',
        artist_id = 2,
        lyrics = """[Intro]<br />
Duh-duh-duh, duh, duh, duh<br />
As he falls back deeper, into a state<br />
The return (Dot Da Genius, baby)<br />
(Daytrip took it to ten, hey)<br />
<br />l
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
        image = 'https://nqg-images.s3.amazonaws.com/Bliding_lights-01.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/The_Weeknd_Blinding_Lights_preview.mp3',
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
        Song(
        title = 'You Should Be Sad',
        artist_id = 4,
        image = 'https://nqg-images.s3.amazonaws.com/Manic.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Halsey_You_Should_Be_Sad.mp3',
        lyrics = """[Verse 1]<br />
I wanna start this out and say<br />
I gotta get it off my chest (My chest)<br />
Got no anger, got no malice<br />
Just a little bit of regret (Regret)<br />
Know nobody else will tell you<br />
So there's some things I gotta say<br />
Gonna jot it down and then get it out<br />
And then I'll be on my way<br />
<br />
[Pre-Chorus]<br />
No, you're not half the man you think that you are<br />
And you can't fill the hole inside of you with money, drugs, and cars<br />
I'm so glad I never ever had a baby with you<br />
'Cause you can't love nothing unless there's something in it for you<br />
<br />
[Chorus]<br />
Oh, I feel so sorry, I feel so sad<br />
I tried to help you, it just made you mad<br />
And I had no warning about who you are<br />
I'm just glad I made it out without breaking down<br />
And then ran so fucking far<br />
That you would never ever touch me again<br />
Won't see your alligator tears<br />
'Cause know I've had enough of them<br />
<br />
[Verse 2]<br />
I'm gonna start this out by saying (By saying)<br />
I really meant well from the start<br />
Take a broken man right in my hands<br />
And then put back all his parts<br />
<br />
[Pre-Chorus]<br />
But you're not half the man you think that you are<br />
And you can't fill the hole inside of you with money, girls, and cars<br />
I'm so glad I never ever had a baby with you<br />
'Cause you can't love nothing unless there's something in it for you<br />
<br />
[Chorus]<br />
Oh, I feel so sorry (I feel so sorry)<br />
I feel so sad (I feel so sad)<br />
I tried to help you (I tried to help you)<br />
It just made you mad<br />
And I had no warning (I had no warning)<br />
About who you are (About who you are)<br />
Just glad I made it out without breaking down<br />
Oh, I feel so sorry (I feel so sorry)<br />
I feel so sad (I feel so sad)<br />
I tried to help you (I tried to help you)<br />
It just made you mad<br />
And I had no warning (I had no warning)<br />
About who you are (About who you are)<br />
'Bout who you are<br />
<br />
[Bridge]<br />
Hey-ey-ey-ey, yeah<br />
Hey-ey-ey-ey, yeah<br />
Hey-ey-ey-ey, yeah<br />
Hey-ey-ey-ey, yeah<br />
<br />
[Pre-Chorus]<br />
'Cause you're not half the man you think that you are<br />
And you can't fill the hole inside of you with money, drugs, and cars<br />
I'm so glad I never ever had a baby with you<br />
'Cause you can't love nothing unless there's something in it for you<br />
<br />
[Outro]<br />
I feel so sad<br />
You should be sad<br />
You should be<br />
You should be sad<br />
You should be<br />
You should be<br />
You should be[Intro]<br />
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
No, I can't sleep until I feel your touch[Verse 1]<br />
I wanna start this out and say<br />
I gotta get it off my chest (My chest)<br />
Got no anger, got no malice<br />
Just a little bit of regret (Regret)<br />
Know nobody else will tell you<br />
So there's some things I gotta say<br />
Gonna jot it down and then get it out<br />
And then I'll be on my way<br />
<br />
[Pre-Chorus]<br />
No, you're not half the man you think that you are<br />
And you can't fill the hole inside of you with money, drugs, and cars<br />
I'm so glad I never ever had a baby with you<br />
'Cause you can't love nothing unless there's something in it for you<br />
<br />
[Chorus]<br />
Oh, I feel so sorry, I feel so sad<br />
I tried to help you, it just made you mad<br />
And I had no warning about who you are<br />
I'm just glad I made it out without breaking down<br />
And then ran so fucking far<br />
That you would never ever touch me again<br />
Won't see your alligator tears<br />
'Cause know I've had enough of them<br />
<br />
[Verse 2]<br />
I'm gonna start this out by saying (By saying)<br />
I really meant well from the start<br />
Take a broken man right in my hands<br />
And then put back all his parts<br />
<br />
[Pre-Chorus]<br />
But you're not half the man you think that you are<br />
And you can't fill the hole inside of you with money, girls, and cars<br />
I'm so glad I never ever had a baby with you<br />
'Cause you can't love nothing unless there's something in it for you<br />
<br />
[Chorus]<br />
Oh, I feel so sorry (I feel so sorry)<br />
I feel so sad (I feel so sad)<br />
I tried to help you (I tried to help you)<br />
It just made you mad<br />
And I had no warning (I had no warning)<br />
About who you are (About who you are)<br />
Just glad I made it out without breaking down<br />
Oh, I feel so sorry (I feel so sorry)<br />
I feel so sad (I feel so sad)<br />
I tried to help you (I tried to help you)<br />
It just made you mad<br />
And I had no warning (I had no warning)<br />
About who you are (About who you are)<br />
'Bout who you are<br />
<br />
[Bridge]<br />
Hey-ey-ey-ey, yeah<br />
Hey-ey-ey-ey, yeah<br />
Hey-ey-ey-ey, yeah<br />
Hey-ey-ey-ey, yeah<br />
<br />
[Pre-Chorus]<br />
'Cause you're not half the man you think that you are<br />
And you can't fill the hole inside of you with money, drugs, and cars<br />
I'm so glad I never ever had a baby with you<br />
'Cause you can't love nothing unless there's something in it for you<br />
<br />
[Outro]<br />
I feel so sad<br />
You should be sad<br />
You should be<br />
You should be sad<br />
You should be<br />
You should be<br />
You should be"""
        ),

        Song(
        title = 'No Time To Die',
        artist_id = 5,
        image = 'https://nqg-images.s3.amazonaws.com/No_Time_To_Die-01.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Billie_Eilish_No_Time_To_Die.mp3',
        lyrics = """[Verse 1]<br />
I should have known<br />
I'd leave alone<br />
Just goes to show<br />
That the blood you bleed is just the blood you owe<br />
We were a pair<br />
But I saw you there<br />
Too much to bear<br />
You were my life, but life is far away from fair<br />
Was I stupid to love you?<br />
Was I reckless to help?<br />
Was it obvious to everybody else?<br />
<br />
[Chorus]<br />
That I'd fallen for a lie<br />
You were never on my side<br />
Fool me once, fool me twice<br />
Are you death or paradise?<br />
Now you'll never see me cry<br />
There's just no time to die<br />
<br />
[Verse 2]<br />
I let it burn<br />
You're no longer my concern, mmm<br />
Faces from my past return<br />
Another lesson yet to learn<br />
<br />
[Chorus]<br />
That I'd fallen for a lie<br />
You were never on my side<br />
Fool me once, fool me twice<br />
Are you death or paradise?<br />
Now you'll never see me cry<br />
There's just no time to die<br />
<br />
[Refrain]<br />
No time to die, mmm<br />
No time to die, ooh<br />
<br />
[Outro]<br />
Fool me once, fool me twice<br />
Are you death or paradise?<br />
Now you'll never see me cry<br />
There's just no time to die"""
        ),

        Song(
        title = 'Roses',
        artist_id = 6,
        image = 'https://nqg-images.s3.amazonaws.com/While_The_World_Was_Burning.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/SAINt_JHN_Roses_Imanbek_Remix.mp3',
        lyrics = """[Verse 1]<br />
Roses<br />
I walked in the corner with the body screaming dolo<br />
Never sold a bag but look like Pablo in a photo<br />
This gon' make 'em feel the way like Tony killed Manolo<br />
You already know though, you already know though<br />
I walk in the corner with the money, on my finger<br />
She might get it popping, I might wife her for the winter<br />
I already know, already know, nigga roses<br />
All I need is roses<br />
<br />
[Chorus]<br />
Turn up baby, turn up, when I turn it on<br />
You know how I get too lit when I turn it on<br />
Can't handle my behavior when I turn it on<br />
Too fast, never ask, if the life don't last<br />
Done been through it all<br />
Fuck with a nigga raw, this who you wanna be<br />
And I know you won't tell nobody nothing<br />
And I know you won't tell nobody no<br />
<br />
[Verse 2]<br />
Roses<br />
I might pull up flexing on these niggas like aerobics<br />
I might tell her girl you cute but balling<br />
That shit gorgeous<br />
Standing on the table, Rosé, Rosé, fuck the waters<br />
You know who the god is<br />
<br />
[Chorus]<br />
Turn up baby, turn up, when I turn it on<br />
You know how I get too lit when I turn it on<br />
Can't handle my behavior when I turn it on<br />
Too fast, never ask, if the life don't last<br />
Done been through it all<br />
Fuck with a nigga raw<br />
<br />
[Verse 3]<br />
I might bring them Brooklyn niggas out, oh lord it's overs<br />
I might bring them strippers out and tell 'em do it pole-less<br />
You already know, already know, nigga roses<br />
Kill 'em, make it ...<br />
<br />
[Chorus]<br />
Turn up baby, turn up, when I turn it on<br />
You know how I get too lit when I turn it on<br />
Can't handle my behavior when I turn it on<br />
Too fast, never ask, if the life don't last<br />
Done been through it all<br />
Fuck with a nigga raw, this who you wanna be<br />
And I know you won't tell nobody nothing<br />
And I know you won't tell nobody no<br />
<br />
[Outro]<br />
Roses<br />
Roses"""
        ),

        Song(
        title = 'Life is Good (feat. Drake)',
        artist_id = 7,
        image = 'https://nqg-images.s3.amazonaws.com/High_Off_Life.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Future_Drake_Life_Is_Good.mp3',
        lyrics = """[Part I]<br />
<br />
[Chorus: Drake]<br />
Workin' on a weekend like usual<br />
Way off in the deep end like usual<br />
Niggas swear they passed us, they doin' too much<br />
Haven't done my taxes, I'm too turnt up<br />
Virgil got a Patek on my wrist goin' nuts<br />
Niggas caught me slippin' once, okay, so what?<br />
Someone hit your block up, I'd tell you if it was us<br />
Manor house in Rosewood, this shit too plush<br />
<br />
[Verse: Drake]<br />
Say my days are numbered, but I keep wakin' up<br />
Know you see my texts, baby, please say some<br />
Wine by the glass, your man a cheapskate, huh?<br />
Niggas gotta move off my release day, huh<br />
Bitch, this is fame, not clout<br />
I don't even know what that's about, watch your mouth<br />
Baby got a ego twice the size of the crib<br />
I can never tell her shit, it is what it is (What)<br />
Said what I had to and did what I did (Ayy)<br />
Never turn my back on FBG, God forbid<br />
Virgil got the Patek on my wrist doin' front flips<br />
Givin' you my number, but don't hit me on no dumb shit<br />
<br />
[Chorus: Drake]<br />
Workin' on a weekend like usual<br />
Way off in the deep end like usual (Like usual)<br />
Niggas swear they passed us, they doin' too much<br />
Haven't done my taxes, I'm too turnt up<br />
Virgil got a Patek on my wrist goin' nuts<br />
Niggas caught me slippin' once, okay, so what?<br />
Someone hit your block up, I'd tell you if it was us<br />
Manor house in Rosewood, this shit too plush<br />
<br />
[Interlude: Future]<br />
It's cool, man, got red bottoms on<br />
Life is good, you know what I mean? Like<br />
<br />
[Part II]<br />
<br />
[Chorus: Future]<br />
Yeah, hunnid thousand for the cheapest ring on a nigga finger, lil' bitch, woo<br />
I done flew one out to Spain to be in my domain and Audemars-ed the bitch, woo<br />
Dropped three dollars on a ring, cost a Bentley truck, lil' bitch, woo<br />
I was in the trap servin' cocaine, I ain't been the same since, woo<br />
<br />
[Verse 1: Future]<br />
Granny, she was standin' right there while I catch a play on a brick, woo<br />
I make them lil' niggas go haywire, Taliban in this bitch, woo<br />
I done been down bad in them trenches, had to ride with that stick, woo<br />
Who gave you pills? Who gave you that dust? Pluto sent you on a lick, woo<br />
Too many convicts that roll with me to play in this shit, woo<br />
I'm tryna avoid nonsense, get Osama spray in this bitch, woo<br />
They at the candlelight lightin' it up, nigga, anybody can get it, woo<br />
I'm on a PJ lightin' it up, Backwood full of sticky, woo<br />
I'm tryna tote that Draco in London and it's extended, woo<br />
They gotta stretch a nigga out, we gon' die for this shit, woo<br />
Yeah, I ride for my niggas, I lie to my bitch, woo<br />
We some poor, high-class niggas, made it, we rich, yeah<br />
I was at the bando, got a penthouse for a closet, woo<br />
It's like a chandelier on my neck, my wrist, woo<br />
I got pink toes that talk different languages, woo<br />
Got Promethazine in my blood and Percocet, yeah<br />
<br />
[Chorus: Future]<br />
Hunnid thousand for the cheapest ring on a nigga finger, lil' bitch, woo<br />
I done flew one out to Spain to be in my domain and Audemars-ed the bitch, woo<br />
Dropped three dollars on a ring, cost a Bentley truck, lil' bitch, woo<br />
I was in the trap servin' cocaine, I ain't been the same since, woo<br />
<br />
[Verse 2: Future]<br />
Racks by the ton, I call up Serena<br />
I go tremendo for new fettuccine<br />
All fact though, carat the pinky<br />
All fact though, we ordered the Fiji<br />
I'm in the loop with the voo, I'm in the loop with the woo, which one you workin'?<br />
I'll put your face on the news, I'll put the pussy on the shirt after I murk it<br />
Then make 'em go shoot up the hearse, cost me a quarter bird, nigga, it's worth it<br />
And you a maniac, a fuckin' alien, how you splurgin'?<br />
Got that kitty cat, I'm havin' fun with that, goin' Birkin<br />
<br />
[Chorus: Future]<br />
Yeah, hunnid thousand for the cheapest ring on a nigga finger, lil' bitch, woo<br />
I done flew one out to Spain to be in my domain and Audemars-ed the bitch, woo<br />
Dropped three dollars on a ring, cost a Bentley truck, lil' bitch, woo<br />
I was in the trap servin' cocaine, I ain't been the same since, woo<br />
<br />
[Outro: Future]<br />
Hunnid thousand for the cheapest ring on a nigga finger, lil' bitch<br />
Hunnid thousand for the cheapest ring on a nigga finger, lil' bitch, yeah<br />
Hunnid thousand for the cheapest ring on a nigga finger, lil' bitch, uh<br />
Hunnid thousand for the cheapest ring on a nigga finger, lil' bitch"""
        ),


        Song(
        title = 'Breathe Deeper',
        artist_id = 8,
        image = 'https://nqg-images.s3.amazonaws.com/The_Slow_Rush-01.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Tame_Impala_Breathe_Deeper.mp3',
        lyrics = """[Verse 1]<br />
If you think I couldn't hold my own, believe me, I can<br />
Believe me, I can, believe me, I can<br />
If it ain't so awful and we're all together, I can<br />
Believe me, I can, believe me, I can<br />
If you think I couldn't roll with you, believe me, I can<br />
Believe me, I can, believe me, I can<br />
If ideally we should feel like this forever, I can<br />
Believe me, I can, believe me, I can<br />
<br />
[Chorus]<br />
(And she said) Seems you're coming on<br />
Breathe a little deeper<br />
Should you need to come undone<br />
And let those colours run<br />
(And she said) Now you're having fun<br />
So do this and get through this<br />
And come find me when you're done<br />
So we can be as one<br />
<br />
[Verse 2]<br />
If you think I couldn't hold my own, believe me, I can<br />
Believe me, I can, believe me, I can<br />
If you need someone to tell you that you're special, I can<br />
Believe me, I can, believe me, I can<br />
If you need someone to carry on, believe me, I can<br />
Believe me, I can, believe me, I can<br />
If you think no one is feeling what you're feeling, I am<br />
Believe me, I am, believe me, I am<br />
<br />
[Bridge]<br />
And the groove is low<br />
<br />
[Chorus]<br />
(And she said) Seems you're coming on<br />
Breathe a little deeper<br />
Should you need to come undone<br />
And let those colours run<br />
Now you're having fun<br />
So do this and get through this (And the groove is low)<br />
And come find me when you're done<br />
So we can be as one<br />
<br />
[Refrain]<br />
Telemona<br />
Telemona, oh<br />
And the groove is low<br />
Telemona<br />
And the groove is low<br />
<br />
[Chorus]<br />
Seems you're coming on<br />
Breathe a little deeper<br />
Should you need to come undone (Telamona)<br />
And let those colours run<br />
Now you're having fun (Telamona)<br />
Do this and get through this<br />
And until we see the sun (And the groove is low)<br />
You're my number one<br />
<br />
[Refrain]<br />
Telemona<br />
(And she said)<br />
And the groove is low<br />
Telemona<br />
And the groove is low<br />
<br />
[Outro]<br />
We're both adults while we behave like children<br />
Long as we got enough to keep on living<br />
Telemona<br />
Telemona"""
        ),

        Song(
        title = 'Murder Most Foul',
        artist_id = 9,
        image = 'https://nqg-images.s3.amazonaws.com/Rough_And_Rowdy_Ways.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Bob_Dylan_Murder_Most_Foul.mp3',
        lyrics = """[Verse 1]<br />
'Twas a dark day in Dallas, November '63<br />
A day that will live on in infamy<br />
President Kennedy was a-ridin' high<br />
Good day to be livin' and a good day to die<br />
Being led to the slaughter like a sacrificial lamb<br />
He said, "Wait a minute, boys, you know who I am?"<br />
"Of course we do, we know who you are"<br />
Then they blew off his head while he was still in the car<br />
Shot down like a dog in broad daylight<br />
Was a matter of timing and the timing was right<br />
You got unpaid debts, we've come to collect<br />
We're gonna kill you with hatred, without any respect<br />
We'll mock you and shock you and we'll grin in your face<br />
We've already got someone here to take your place<br />
The day they blew out the brains of the king<br />
Thousands were watching, no one saw a thing<br />
It happened so quickly, so quick, by surprise<br />
Right there in front of everyone's eyes<br />
Greatest magic trick ever under the sun<br />
Perfectly executed, skillfully done<br />
Wolfman, oh Wolfman, oh Wolfman, howl<br />
Rub-a-dub-dub, it's a murder most foul<br />
<br />
[Verse 2]<br />
Hush, little children, you'll understand<br />
The Beatles are comin', they're gonna hold your hand<br />
Slide down the banister, go get your coat<br />
Ferry 'cross the Mersey and go for the throat<br />
There's three bums comin' all dressed in rags<br />
Pick up the pieces and lower the flags<br />
I'm goin' to Woodstock, it's the Aquarian Age<br />
Then I'll go over to Altamont and sit near the stage<br />
Put your head out the window, let the good times roll<br />
There's a party going on behind the Grassy Knoll<br />
Stack up the bricks, pour the cement<br />
Don't say Dallas don't love you, Mr. President<br />
Put your foot in the tank and then step on the gas<br />
Try to make it to the triple underpass<br />
Blackface singer, whiteface clown<br />
Better not show your faces after the sun goes down<br />
Up in the red light district, like a cop on the beat<br />
Living in a nightmare on Elm Street<br />
When you're down on Deep Ellum, put your money in your shoe<br />
Don't ask what your country can do for you<br />
Cash on the barrelhead, money to burn<br />
Dealey Plaza, make a left-hand turn<br />
I'm going down to the crossroads, gonna flag a ride<br />
The place where faith, hope, and charity died<br />
Shoot him while he runs, boy, shoot him while you can<br />
See if you can shoot the invisible man<br />
Goodbye, Charlie, goodbye, Uncle Sam<br />
Frankly, Miss Scarlett, I don't give a damn<br />
What is the truth, and where did it go?<br />
Ask Oswald and Ruby, they oughta know<br />
"Shut your mouth," said a wise old owl<br />
Business is business, and it's a murder most foul<br />
<br />
[Verse 3]<br />
Tommy, can you hear me? I'm the Acid Queen<br />
I'm riding in a long, black Lincoln limousine<br />
Ridin' in the back seat next to my wife<br />
Headed straight on in to the afterlife<br />
I'm leaning to the left, I got my head in her lap<br />
Oh Lord, I've been led into some kind of a trap<br />
Where we ask no quarter, and no quarter do we give<br />
We're right down the street, from the street where you live<br />
They mutilated his body and they took out his brain<br />
What more could they do? They piled on the pain<br />
But his soul was not there where it was supposed to be at<br />
For the last fifty years they've been searchin' for that<br />
Freedom, oh freedom, freedom over me<br />
I hate to tell you, mister, but only dead men are free<br />
Send me some lovin', then tell me no lie<br />
Throw the gun in the gutter and walk on by<br />
Wake up, little Susie, let's go for a drive<br />
Cross the Trinity River, let's keep hope alive<br />
Turn the radio on, don't touch the dials<br />
Parkland Hospital, only six more miles<br />
You got me dizzy, Miss Lizzy, you filled me with lead<br />
That magic bullet of yours has gone to my head<br />
I'm just a patsy like Patsy Cline<br />
Never shot anyone from in front or behind<br />
I've blood in my eye, got blood in my ear<br />
I'm never gonna make it to the new frontier<br />
Zapruder's film, I've seen that before<br />
Seen it thirty-three times, maybe more<br />
It's vile and deceitful, it's cruel and it's mean<br />
Ugliest thing that you ever have seen<br />
They killed him once and they killed him twice<br />
Killed him like a human sacrifice<br />
The day that they killed him, someone said to me, "Son<br />
The age of the Antichrist has just only begun"<br />
Air Force One comin' in through the gate<br />
Johnson sworn in at 2:38<br />
Let me know when you decide to throw in the towel<br />
It is what it is, and it's murder most foul<br />
<br />
[Verse 4]<br />
What's new, pussycat? What'd I say?<br />
I said the soul of a nation been torn away<br />
And it's beginning to go into a slow decay<br />
And that it's thirty-six hours past Judgment Day<br />
Wolfman Jack, he's speaking in tongues<br />
He's going on and on at the top of his lungs<br />
Play me a song, Mr. Wolfman Jack<br />
Play it for me in my long Cadillac<br />
Play me that "Only the Good Die Young"<br />
Take me to the place Tom Dooley was hung<br />
Play "St. James Infirmary" in the Court of King James<br />
If you want to remember, you better write down the names<br />
Play Etta James, too, play "I'd Rather Go Blind"<br />
Play it for the man with the telepathic mind<br />
Play John Lee Hooker, play "Scratch My Back"<br />
Play it for that strip club owner named Jack<br />
Guitar Slim going down slow<br />
Play it for me and for Marilyn Monroe<br />
<br />
[Verse 5]<br />
Play "Please Don't Let Me Be Misunderstood"<br />
Play it for the First Lady, she ain't feeling any good<br />
Play Don Henley, play Glenn Frey<br />
Take it to the limit and let it go by<br />
Play it for Carl Wilson, too<br />
Looking far, far away down Gower Avenue<br />
Play "Tragedy", play "Twilight Time"<br />
Take me back to Tulsa to the scene of the crime<br />
Play another one and "Another One Bites the Dust"<br />
Play "The Old Rugged Cross" and "In God We Trust"<br />
Ride the pink horse down that long, lonesome road<br />
Stand there and wait for his head to explode<br />
Play "Mystery Train" for Mr. Mystery<br />
The man who fell down dead like a rootless tree<br />
Play it for the reverend, play it for the pastor<br />
Play it for the dog that got no master<br />
Play Oscar Peterson, play Stan Getz<br />
Play "Blue Sky," play Dickey Betts<br />
Play Art Pepper, Thelonious Monk<br />
Charlie Parker and all that junk<br />
All that junk and "All That Jazz"<br />
Play something for the Birdman of Alcatraz<br />
Play Buster Keaton, play Harold Lloyd<br />
Play Bugsy Siegel, play Pretty Boy Floyd<br />
Play the numbers, play the odds<br />
Play "Cry Me a River" for the Lord of the gods<br />
Play Number nine, play Number six<br />
Play it for Lindsey and Stevie Nicks<br />
Play Nat King Cole, play "Nature Boy"<br />
Play "Down in the Boondocks" for Terry Malloy<br />
Play "It Happened One Night" and "One Night of Sin"<br />
There's twelve million souls that are listening in<br />
Play "Merchant of Venice", play "Merchants of Death"<br />
Play "Stella by Starlight" for Lady Macbeth<br />
Don't worry, Mr. President, help's on the way<br />
Your brothers are comin', there'll be hell to pay<br />
Brothers? What brothers? What's this about hell?<br />
Tell them, "We're waiting, keep coming," we'll get them as well<br />
Love Field is where his plane touched down<br />
But it never did get back up off the ground<br />
Was a hard act to follow, second to none<br />
They killed him on the altar of the rising sun<br />
Play "Misty" for me and "That Old Devil Moon"<br />
Play "Anything Goes" and "Memphis in June"<br />
Play "Lonely at the Top" and "Lonely Are the Brave"<br />
Play it for Houdini spinning around in his grave<br />
Play Jelly Roll Morton, play "Lucille"<br />
Play "Deep in a Dream", and play "Driving Wheel"<br />
Play "Moonlight Sonata" in F-sharp<br />
And "A Key to the Highway" for the king on the harp<br />
Play "Marching Through Georgia" and "Dumbarton's Drums"<br />
Play "Darkness" and death will come when it comes<br />
Play "Love Me or Leave Me" by the great Bud Powell<br />
Play "The Blood-Stained Banner", play "Murder Most Foul"""
        ),

        Song(
        title = 'The Bones',
        artist_id = 10,
        image = 'https://nqg-images.s3.amazonaws.com/GIRL.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Maren_Morris_The_Bones.mp3',
        lyrics = """[Verse 1]<br />
We're in the homestretch of the hard times<br />
We took a hard left, but we're alright<br />
Yeah, life sure can try to put love through it, but<br />
We built this right, so nothing's ever gonna move it<br />
<br />
[Chorus]<br />
When the bones are good, the rest don't matter<br />
Yeah, the paint could peel, the glass could shatter<br />
Let it rain 'cause you and I remain the same<br />
When there ain't a crack in the foundation<br />
Baby, I know any storm we're facing<br />
Will blow right over while we stay put<br />
The house don't fall when the bones are good<br />
<br />
[Verse 2]<br />
Call it dumb luck, but baby, you and I<br />
Can't even mess it up, yeah, though we both tried<br />
No, it don't always go the way we planned it<br />
But the wolves came and went and we're still standing<br />
<br />
[Chorus]<br />
When the bones are good, the rest don't matter<br />
Yeah, the paint could peel, the glass could shatter<br />
Let it rain 'cause you and I remain the same<br />
When there ain't a crack in the foundation<br />
Baby, I know any storm we're facing<br />
Will blow right over while we stay put<br />
The house don't fall when the bones are good<br />
When the bones are good<br />
<br />
[Bridge]<br />
Bones are good, the rest, the rest don't matter (Baby, it don't really matter)<br />
Paint could peel, the glass, the glass could shatter (Oh, the glass, oh, the glass could shatter)<br />
Bones are good, the rest, the rest don't matter (Ooh)<br />
Paint could peel, the glass, the glass could shatter (Yeah)<br />
<br />
[Chorus]<br />
When the bones are good, the rest don't matter<br />
Yeah, the paint could peel, the glass could shatter<br />
Let it rain (Let it rain, let it rain)<br />
'Cause you and I remain the same (Woo)<br />
When there ain't a crack in the foundation (Woo)<br />
Baby, I know any storm we're facing<br />
Will blow right over while we stay put<br />
The house don't fall when the bones are good<br />
<br />
[Outro]<br />
Yeah, ooh"""
        ),

        Song(
        title = 'On the Floor',
        artist_id = 11,
        image = 'https://nqg-images.s3.amazonaws.com/SMHOFI.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Perfume_Genius_On_The_Floor.mp3',
        lyrics = """I'm trying, but still, I close my eyes (Mmm)<br />
The dreaming, bringing his face to mine<br />
<br />
Lock the door<br />
The constant buzzing all through the night (Mmm)<br />
The fighting rips me all up inside<br />
<br />
On the floor<br />
I pace, I run my mouth<br />
I pray and wait<br />
I cross out his name on the page<br />
<br />
How long 'til this washes away?<br />
How long 'til my body is safe?<br />
How long 'til I walk in the light?<br />
How long 'til this heart isn’t mine?<br />
<br />
The rise and fall of his chest on me (Mmm)<br />
I'm trying, but still, it's all I see<br />
The violent current of energy (Mmm)<br />
I hide it away and underneath<br />
<br />
Lock the door<br />
I shake, I promise every day to change<br />
I cross out his name on the page<br />
<br />
How long 'til this washes away?<br />
How long 'til my body is safe?<br />
How long 'til I walk in the light?<br />
How long 'til this heart isn’t mine?<br />
<br />
Take this wildness away<br />
Wildness away<br />
Wildness away<br />
Ah, ah<br />
<br />
I'm trying, but still, I close my eyes (Mmm)<br />
The dreaming, bringing his face to mine<br />
<br />
Out the door<br />
I pace, I run my mouth<br />
I pray to change<br />
I cross out his name on the page<br />
<br />
How long 'til this washes away?<br />
How long 'til my body is safe?<br />
How long 'til this heart isn't mine?<br />
<br />
I just want him in my arms<br />
I just want him in my arms"""
        ),

        Song(
        title = 'Yo Perreo Sola (English translation)',
        artist_id = 12,
        image = 'https://nqg-images.s3.amazonaws.com/YHLQMDLG.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Yo_Perreo_Sola_Bad_Bunny.mp3',
        lyrics = """[Pre-Chorus: Nesi]<br />
You used to ignore me (You ignored me)<br />
Now I ignore you (Hmm, nah)<br />
Before, you didn't want to (Didn't want to)<br />
Now I don't want (Hmm, no)<br />
You used to ignore me (-nored me)<br />
Now I ignore you (Haha)<br />
Before, you didn't want to (Ayy)<br />
Now I don't want to<br />
No, chill<br />
<br />
[Chorus: Nesi & Bad Bunny]<br />
I twerk alone (Hmm, ayy)<br />
I twerk alone (Twerk alone, haha, hmm-hmm)<br />
I twerk alone (Haha, hmm, ayy)<br />
I twerk alone (Twerk alone)<br />
Okay, okay, ayy, ayy, ayy<br />
<br />
[Verse 1: Bad Bunny]<br />
Perverts, don't get near her (No)<br />
The club turns up when she arrives (Woo!)<br />
Men are her hobby<br />
She is spoiled like Nairobi (Haha)<br />
And you see her drinking from the bottle (Ayy)<br />
The boys and the girls want to get it with her<br />
She is older than twenty, she showed me her ID (Uh-huh)<br />
Ayy, she is skeptical of love (Woo!)<br />
She's been single before it was a trend (Ayy)<br />
She doesn't believe in love since "Amorfoda" (No)<br />
The DJ plays songs and she knows them all<br />
She climbs on the table and doesn't give a fuck about anyone (Woo)<br />
When she twerks she doesn't stop (No!)<br />
She smokes and gets horny<br />
She'll call you if she needs you<br />
But for now she is alone<br />
<br />
[Chorus: Bad Bunny]<br />
She twerks alone (Woo)<br />
Ayy, ayy, ayy, ayy, ayy, ayy<br />
She twerks alone<br />
(Twerks alone, she twerks alone, alone, alone)<br />
Ayy, she twerks alone<br />
Ayy, ayy, ayy, ayy, ayy, ayy<br />
She twerks alone (She twerks alone)<br />
She twerks alone<br />
<br />
[Verse 2: Bad Bunny]<br />
She has a problematic friend<br />
And another one that almost never talks (No)<br />
But the three of them are bad (Prr)<br />
And today she is wearing a miniskirt<br />
She keeps her Phillies in the Louis Vuitton<br />
<br />
[Bridge: Bad Bunny & Nesi]<br />
And she calls me "papi" (Papi, keep going, yes, yes)<br />
She's really hot like Natti (Ah)<br />
Drunk and crazy, she doesn't care (Woo)<br />
Let's twerk, life is short, ayy (Hoo)<br />
And she calls me "papi" (Papi, keep going, yes, yes)<br />
She's really hot like Natti (Ah)<br />
After twelve o'clock she doesn't behave (Ayy)<br />
Let's twerk, life is short (Woo)<br />
<br />
[Pre-Chorus: Nesi & Bad Bunny]<br />
You used to ignore me (You ignored me)<br />
Now I ignore you (Hmm, nah, crazy)<br />
Before, you didn't want to (But when did I say that?)<br />
Now I don't want to (But, but, no)<br />
You used to ignore me (Nah)<br />
Now I ignore you (I've never ignored you, babe)<br />
Before you didn't want to (Oh, God)<br />
Now I don't want to<br />
No, chill<br />
<br />
[Chorus: Nesi]<br />
I twerk alone (Hmm, ayy)<br />
I twerk alone (Twerk alone, haha, hmm-hmm)<br />
I twerk alone (Haha, hmm, ayy)<br />
I twerk alone (Twerk alone)"""
        ),

        Song(
        title = 'Ladies',
        artist_id = 13,
        image = 'https://nqg-images.s3.amazonaws.com/Fetch_The_Boltcutters.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Fiona_Apple_Ladies.mp3',
        lyrics = """[Intro]<br />
Ladies, ladies, ladies, ladies<br />
Ladies, ladies, ladies, ladies<br />
Ladies, ladies, ladies, ladies<br />
Ladies, ladies, ladies, ladies<br />
<br />
[Verse 1]<br />
Ruminations on the looming effect and the parallax view<br />
And the figure and the form and the revolving door that keeps<br />
Turning out more and more good women like you<br />
Yet another woman to whom I won't get through<br />
Ruminations on the looming effect and the parallax view<br />
And the figure and the form and the revolving door that keeps<br />
Turning out more and more good women like you<br />
Yet another woman to whom I won't get through<br />
<br />
[Verse 2]<br />
Ladies, ladies, ladies, ladies, take it easy<br />
When he leaves me, please be my guest<br />
To whatever I might've left in his kitchen cupboards<br />
In the back of his bathroom cabinets<br />
<br />
[Verse 3]<br />
And oh yes, oh yes, oh yes<br />
There's a dress in the closet<br />
Don't get rid of it, you'd look good in it<br />
I didn't fit in it, it was never mine<br />
It belonged to the ex-wife of another ex of mine<br />
She left it behind with a note, one line, it said<br />
"I don't know if I'm coming across, but I'm really trying"<br />
She was very kind<br />
<br />
[Chorus]<br />
Fruit bat<br />
Cuter than a button, mutton-head maniac<br />
Fruit bat<br />
Cuter than a button, mutton-head maniac<br />
<br />
[Verse 4]<br />
Nobody can replace anybody else<br />
So it would be a shame to make it a competition<br />
And no love is like any other love<br />
So it would be insane to make a comparison with you<br />
<br />
[Verse 5]<br />
Ruminations on the looming effect and the parallax view<br />
And the figure and the form and the revolving door that keeps<br />
Turning out more and more good women like you<br />
Yet another woman to whom I won't get through<br />
<br />
[Chorus]<br />
Ooh<br />
Cuter than a button, mutton-head maniac<br />
<br />
[Refrain]<br />
Ladies, ladies, ladies, ladies<br />
Ladies, ladies, ladies, ladies<br />
Ladies, ladies, ladies, ladies<br />
Ladies, ladies, ladies, ladies<br />
<br />
[Verse 6]<br />
And no love is like any other love<br />
So it would be insane to make a comparison with you<br />
<br />
[Refrain]<br />
Ladies, ladies, ladies, ladies<br />
Ladies, ladies, ladies, ladies<br />
Ladies, ladies, ladies, ladies<br />
<br />
[Outro]<br />
Yet another woman to whom I won't get through<br />
Yet another woman to whom I won't get through<br />
Yet another woman to whom I won't get through<br />
Yet another woman to whom I won't get through<br />
Yet another woman to whom I won't get through"""
        ),

        Song(
        title = 'Good News',
        artist_id = 14,
        image = 'https://nqg-images.s3.amazonaws.com/Circles.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Mac_Miller_Good_News.mp3',
        lyrics = """[Verse 1]<br />
I spent the whole day in my head<br />
Do a little spring cleanin'<br />
I'm always too busy dreamin'<br />
Well, maybe I should wake up instead<br />
A lot of things I regret, but I just say I forget<br />
Why can't it just be easy?<br />
Why does everybody need me to stay?<br />
Oh, I hate the feelin'<br />
When you're high, but you're underneath the ceilin'<br />
Got the cards in my hand, I hate dealin', yeah<br />
Get everything I need, then I'm gone, but it ain't stealin'<br />
Can I get a break?<br />
I wish that I could just get out my goddamn way<br />
What is there to say?<br />
There ain't a better time than today<br />
Well, maybe I'll lay down for a little, yeah<br />
Instead of always tryin' to figure everything out<br />
And all I do is say sorry<br />
Half the time I don't even know what I'm sayin' it about<br />
<br />
[Chorus]<br />
Good news, good news, good news<br />
That's all they wanna hear<br />
No, they don't like it when I'm down<br />
But when I'm flyin', oh<br />
It make 'em so uncomfortable<br />
So different, what's the difference?<br />
<br />
[Verse 2]<br />
When it ain't that bad<br />
It could always be worse<br />
I'm runnin' out of gas, hardly anything left<br />
Hope I make it home from work<br />
Well, so tired of bein' so tired<br />
Why I gotta build somethin' beautiful just to go set it on fire?<br />
I'm no liar, but<br />
Sometimes the truth don't sound like the truth<br />
Maybe 'cause it ain't<br />
I just love the way it sound when I say it, yeah<br />
It's what I do<br />
If you know me, it ain't anything new<br />
Wake up to the moon, haven't seen the sun in a while<br />
But I heard that the sky's still blue, yeah<br />
I heard they don't talk about me too much no more<br />
And that's the problem with a closed door<br />
<br />
[Chorus]<br />
Good news, good news, good news<br />
That's all they wanna hear<br />
No, they don't like it when I'm down<br />
But when I'm flyin', oh<br />
It make 'em so uncomfortable<br />
So different, what's the difference?<br />
<br />
[Verse 3]<br />
There's a whole lot more for me waitin' on the other side<br />
I'm always wonderin' if it feel like summer<br />
I know maybe I'm too late, I could make it there some other time<br />
I'll finally discover<br />
That there's a whole lot more for me waitin'<br />
That there's a whole lot more for me waitin'<br />
I know maybe I'm too late, I could make it there some other time<br />
Then I'll finally discover<br />
That it ain't that bad, ain't so bad<br />
Well, it ain't that bad, mm<br />
At least it don't gotta be no more<br />
<br />
[Outro]<br />
No more, no more, no more, no more<br />
No more, no more, no more, no more<br />
Hey, hey<br />
Mm, hey, mm, mm, mm"""
        ),

        Song(
        title = 'Rare',
        artist_id = 15,
        image = 'https://nqg-images.s3.amazonaws.com/Rare.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Selena_Gomez_Rare.mp3',
        lyrics = """[Verse 1]<br />
Baby<br />
You've been so distant from me lately<br />
And lately<br />
Don't even wanna call you "baby"<br />
<br />
[Pre-Chorus]<br />
Saw us gettin' older (Older)<br />
Burnin' toast in the toaster<br />
My ambitions were too high<br />
Waiting up for you upstairs (Upstairs)<br />
Why you act like I'm not there?<br />
Baby, right now it feels like<br />
<br />
[Chorus]<br />
It feels like you don't care<br />
Why don't you recognize I'm so rare?<br />
Always there<br />
You don't do the same for me, that's not fair<br />
I don't have it all<br />
I'm not claiming to<br />
But I know that I'm special (So special), yeah<br />
And I'll bet there's somebody else out there<br />
To tell me I'm rare<br />
To make me feel rare<br />
<br />
[Verse 2]<br />
Baby<br />
Don't make me count up all the reasons to stay with you<br />
No reason<br />
Why you and I are not succeeding, ah-ah (Mmm, ah, ah)<br />
<br />
[Pre-Chorus]<br />
Saw us gettin' older (Oh)<br />
Burnin' toast in the toaster (Ah-ha)<br />
My ambitions were too high (Too high)<br />
Waiting up for you upstairs (Upstairs)<br />
Why you act like I'm not there? (Ah-ha)<br />
Baby, right now it feels like (What?)<br />
<br />
[Chorus]<br />
It feels like you don't care<br />
Why don't you recognize I'm so rare? (I'm so rare)<br />
Always there<br />
You don't do the same for me, that's not fair<br />
I don't have it all<br />
I'm not claiming to<br />
But I know that I'm special (So special), yeah<br />
And I'll bet there's somebody else out there<br />
To tell me I'm rare<br />
To make me feel rare (Yeah, yeah)<br />
<br />
[Bridge]<br />
I'm not gonna beg for you<br />
I'm not gonna let you make me cry (Ah, nah nah, make me cry)<br />
Not getting enough from you (No-oh)<br />
Didn't you know I'm hard to find? (Find, hard to find)<br />
<br />
[Pre-Chorus]<br />
Saw us gettin' older<br />
Burnin' toast in the toaster<br />
My ambitions were too high (Too high)<br />
Waiting up for you upstairs<br />
Why you act like I'm not there?<br />
Baby, right now it feels like<br />
<br />
[Chorus]<br />
It feels like you don't care (You don't care)<br />
Why don't you recognize I'm so rare? (So rare)<br />
I'm always there<br />
You don't do the same for me, that's (That's) not (Not) fair<br />
I don't have it all (I don't have it all)<br />
I'm not claiming to (I'm not claiming to)<br />
But I know that I'm special (So special), yeah<br />
And I'll bet there's somebody else out there<br />
To tell me I'm rare<br />
To make me feel rare (Ooh yeah)<br />
<br />
[Outro]<br />
Ah, ah (So rare)<br />
Rare<br />
Ah, ah<br />
Rare"""
        ),

        Song(
        title = 'Supalonely (feat. Gus Dapperton)',
        artist_id = 16,
        image = 'https://nqg-images.s3.amazonaws.com/Hey_u_x.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/BENEE_Supalonely.mp3',
        lyrics = """[Chorus: BENEE]<br />
I know I fucked up, I'm just a loser<br />
Shouldn't be with ya, guess I'm a quitter<br />
While you're out there drinkin', I'm just here thinkin'<br />
'Bout where I should've been<br />
I've been lonely, mmh, ah, yeah<br />
<br />
[Verse 1: BENEE]<br />
Water pouring down from the ceiling<br />
I knew this would happen, still hard to believe it<br />
Maybe I'm dramatic, I don't wanna seem it<br />
I don't wanna panic<br />
<br />
[Pre-Chorus: BENEE]<br />
I'm a sad girl in this big world, it's a mad world<br />
All of my friends know what's happened, you're a bad thing (Ah)<br />
<br />
[Chorus: BENEE]<br />
I know I fucked up, I'm just a loser<br />
Shouldn't be with ya, guess I'm a quitter<br />
While you're out there drinkin', I'm just here thinkin'<br />
'Bout where I should've been<br />
I've been lonely, mmh, ah, yeah<br />
<br />
[Post-Chorus: BENEE]<br />
La-la-la-la, la-la-la-la<br />
Lonely (I'm a lonely bitch)<br />
La-la-la-la, la-la-la-la<br />
Lonely (Super lonely)<br />
<br />
[Verse 2: BENEE & Gus Dapperton]<br />
Now I'm in the bathtub cryin'<br />
Think I'm slowly sinking<br />
Bubbles in my eyes now<br />
Maybe I'm just dreamin'<br />
Now I'm in the sad club<br />
Just tryna get a back rub (Lonely)<br />
<br />
[Pre-Chorus: BENEE with Gus Dapperton]<br />
I'm a sad girl in this big world, it's a mad world<br />
All of my friends know what's happened, you're a bad thing<br />
<br />
[Chorus: BENEE]<br />
I know I fucked up (Fucked up), I'm just a loser (Loser)<br />
Shouldn't be with ya (With ya), guess I'm a quitter (Quitter)<br />
While you're out there drinkin' (Drinkin'), I'm just here thinkin' (Thinkin')<br />
'Bout where I should've been (Where I should've been)<br />
I've been lonely, mmh, ah, yeah (Woah)<br />
<br />
[Post-Chorus: BENEE]<br />
La-la-la-la (Woo), la-la-la-la<br />
Lonely (I'm a lonely bitch)<br />
La-la-la-la, la-la-la-la<br />
Lonely (Super lonely)<br />
<br />
[Bridge: Gus Dapperton]<br />
I loathe romancing in itself, yeah, I'd be damned to try<br />
I'm only dancin' by myself, so I don't slam my Irish buck<br />
Compostable cups, B-B-BENEE, I can't stress this enough<br />
I would hate to mess things up, but my boogie still stays restless as fuck, yeah<br />
<br />
[Chorus: BENEE & Gus Dapperton, BENEE]<br />
I know I fucked up, I'm just a loser<br />
Shouldn't be with ya, guess I'm a quitter<br />
While you're out there drinkin', I'm just here thinkin'<br />
'Bout where I should've been<br />
I've been lonely, mmh, ah, yeah<br />
<br />
[Post-Chorus: BENEE]<br />
La-la-la-la, la-la-la-la<br />
Lonely (I'm a lonely bitch)<br />
La-la-la-la, la-la-la-la<br />
Lonely (Super lonely)<br />
<br />
[Outro: BENEE]<br />
La-la-la-la, la-la-la-la (I've been lonely, I've been lonely)<br />
Lonely (I've been lonely, by the way)<br />
La-la-la-la, la-la-la-la<br />
Lonely (I've been lonely)"""
        ),

        Song(
        title = 'Gaslighter',
        artist_id = 17,
        image = 'https://nqg-images.s3.amazonaws.com/GasLighter.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Dixie_Chicks_Gaslighter.mp3',
        lyrics = """[Intro]<br />
Gaslighter, denier<br />
Doin' anything to get your ass farther<br />
Gaslighter, big timer<br />
Repeating all of the mistakes of your father<br />
<br />
[Verse 1]<br />
We moved to California and we followed your dreams<br />
I believed in the promises you made to me<br />
Swore that night 'til death do us part<br />
But you lie-lie-lie-lie-lied<br />
Hollywood welcomed you with open doors<br />
No matter what they gave you, you still wanted more<br />
Acting all above it when our friends divorced<br />
What a lie-lie-lie-lie-lie<br />
You're such a<br />
<br />
[Chorus]<br />
Gaslighter, denier<br />
Doin' anything to get your ass farther<br />
Gaslighter, big timer<br />
Repeating all of the mistakes of your father<br />
Gaslighter, you broke me<br />
You're sorry, but where's my apology?<br />
Gaslighter, you liar<br />
<br />
[Verse 2]<br />
You thought I wouldn't see it if you put it in my face<br />
Give you all my money, you'll gladly walk away<br />
You think it's justifiable, I think it's pretty cruel<br />
And you know you lie best when you lie to you<br />
'Cause, boy, you know exactly what you did on my boat<br />
And, boy, that's exactly why you ain't comin' home<br />
Save your tired stories for your new someone else<br />
'Cause they're lie-lie-lie-lie-lies<br />
Look out, you little<br />
<br />
[Chorus]<br />
Gaslighter, denier<br />
Doin' anything to get your ass farther (Ooh)<br />
Gaslighter, big timer<br />
Repeating all of the mistakes of your father<br />
Gaslighter, you broke me<br />
You're sorry, but where's my apology?<br />
Gaslighter, you liar<br />
<br />
[Verse 3]<br />
Just had to start a fire, had to start a fire<br />
Couldn't take yourself on a road a little higher<br />
Had to burn it up, had to tear it down<br />
Tried to say I'm crazy, babe, we know I'm not crazy, that's you<br />
Gaslighting<br />
You're a li-li-li-liar<br />
Oh, honey, that's you<br />
Gaslighting<br />
You made your bed and then your bed caught fire<br />
<br />
[Bridge]<br />
Gaslighter, I'm your mirror<br />
Standin' right here until you can see how you broke me<br />
Yeah, I'm broken<br />
You're still sorry, and there's still no apology<br />
<br />
[Chorus]<br />
Gaslighter, denier (Yeah)<br />
Doin' anything to get your ass farther (Ooh)<br />
Gaslighter, big timer<br />
Repeating all of the mistakes of your father (Gaslighter)<br />
Gaslighter, you broke me<br />
You're sorry, but where's my apology?<br />
Gaslighter, you liar"""
        ),

        Song(
        title = 'Delete Forever',
        artist_id = 18,
        image = 'https://nqg-images.s3.amazonaws.com/Miss_Anthropocene.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Grimes_Delete_Forever.mp3',
        lyrics = """[Verse 1]<br />
Lying so awake, things I can't escape<br />
Lately, I just turn 'em into demons<br />
Flew into the sun, fucking heroin<br />
Lately, I just turn 'em into reasons and excuses<br />
<br />
[Pre-Chorus]<br />
Always down when I'm not up, guess it's just my rotten luck<br />
To fill my time with permanent blue<br />
But I can't see above it, guess I fucking love it<br />
But, oh, I didn't mean to<br />
<br />
[Chorus]<br />
I see everything, I see everything<br />
Don't you tell me now that I don't want it<br />
But I did everything, I did everything<br />
More lines on the mirror than a sonnet (Woo)<br />
<br />
[Verse 2]<br />
Funny how they think us naive when we're on the brink<br />
Innocence was fleeting like a season<br />
Cannot comprehend, lost so many men<br />
Lately, all their ghosts turn into reasons and excuses<br />
<br />
[Pre-Chorus]<br />
Always down when I'm not up, guess it's just my rotten luck<br />
To fill my time with permanent blue<br />
But I can't see above it, guess I fucking love it<br />
But, oh, I didn't mean to<br />
<br />
[Chorus]<br />
I see everything, I see everything<br />
Don't you tell me now that I don't want it<br />
But I did everything, I did everything<br />
More lines on the mirror than a sonnet (Woo)<br />
<br />
[Chorus]<br />
I see everything, I see everything<br />
Don't you tell me now that I don't want it<br />
But I did everything, I did everything<br />
More lines on the mirror than a sonnet"""
        ),

        Song(
        title = 'Physical',
        artist_id = 19,
        image = 'https://nqg-images.s3.amazonaws.com/Future_Nostalgia.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Dua_Lipa_Physical.mp3',
        lyrics = """[Verse 1]<br />
Common love isn't for us<br />
We created something phenomenal<br />
Don't you agree?<br />
Don't you agree?<br />
You got me feeling diamond rich<br />
Nothing on this planet compares to it<br />
Don't you agree?<br />
Don't you agree?<br />
<br />
[Pre-Chorus]<br />
Who needs to go to sleep when I got you next to me?<br />
<br />
[Chorus]<br />
All night, I'll riot with you<br />
I know you got my back and you know I got you<br />
So come on (Come on), come on (Come on), come on (Come on)<br />
Let's get physical<br />
Lights out, follow the noise<br />
Baby, keep on dancing like you ain't got a choice<br />
So come on (Come on), come on (Come on), come on<br />
Let's get physical<br />
<br />
[Verse 2]<br />
Adrenaline keeps on rushing in<br />
Love the simulation we're dreaming in<br />
Don't you agree?<br />
Don't you agree?<br />
I don't wanna live another life<br />
'Cause this one's pretty nice<br />
Living it up<br />
<br />
[Pre-Chorus]<br />
Who needs to go to sleep when I got you next to me?<br />
<br />
[Chorus]<br />
All night, I'll riot with you<br />
I know you got my back and you know I got you<br />
So come on (Come on), come on (Come on), come on (Come on)<br />
Let's get physical<br />
Lights out, follow the noise<br />
Baby, keep on dancing like you ain't got a choice<br />
So come on (Come on), come on (Come on), come on<br />
Let's get physical<br />
<br />
[Bridge]<br />
Hold on just a little tighter<br />
Come on, hold on, tell me if you're ready<br />
Come on (Come on, come on)<br />
Baby, keep on dancing<br />
Let's get physical<br />
Hold on just a little tighter<br />
Come on, hold on, tell me if you're ready<br />
Come on (Come on, come on)<br />
Baby, keep on dancing<br />
Let's get physical<br />
<br />
[Chorus]<br />
All night, I'll riot with you<br />
I know you got my back and you know I got you<br />
So come on, come on, come on<br />
Let's get physical<br />
Lights out, follow the noise<br />
Baby, keep on dancing like you ain't got a choice<br />
So come on (Come on), come on (Come on), come on<br />
Let's get physical (Physical, physical)<br />
<br />
[Outro]<br />
Let's get physical (Physical, physical)<br />
Physical (Physical, physical)<br />
Let's get physical (Physical, physical)<br />
Come on, phy-phy-phy-physical"""
        ),

        Song(
        title = 'Stupid Love',
        artist_id = 20,
        image = 'https://nqg-images.s3.amazonaws.com/Chromatica.png',
        audio_file = 'https://nqg-songs.s3.amazonaws.com/Lady_Gaga_Stupid_Love.mp3',
        lyrics = """[Verse 1]<br />
You're the one that I've been waiting for<br />
Gotta quit this cryin', nobody's gonna<br />
Heal me if I don't open the door<br />
Kinda hard to believe, gotta have faith in me<br />
<br />
[Refrain]<br />
Freak out, freak out, freak out, freak out (Look at me)<br />
Get down, get down, get down, get down (Look at me)<br />
Freak out, freak out, freak out, freak out<br />
Look at me now<br />
<br />
[Pre-Chorus]<br />
'Cause all I ever wanted was love<br />
Hey yeah, hey yeah (Ooh-ooh)<br />
Hey yeah, hey yeah (Ooh-ooh)<br />
Hey yeah, hey yeah<br />
All I ever wanted was love<br />
Hey yeah, hey yeah (Ooh-ooh)<br />
Hey yeah, hey yeah (Ooh-ooh)<br />
Hey yeah, hey yeah, hey yeah (Hey yeah, hey yeah)<br />
<br />
[Chorus]<br />
I want your stupid love, love<br />
I want your stupid love, love<br />
(Oh-oh-oh, oh-oh-oh, oh-oh, oh-oh-oh-oh-oh)<br />
<br />
[Verse 2]<br />
Now, it's time to free me from the shame<br />
I gotta find that peace, is it too late or<br />
Could this love protect me from the pain?<br />
I would battle for you (Even if we break in two)<br />
<br />
[Refrain]<br />
Freak out, freak out, freak out, freak out (Look at me)<br />
Get down, get down, get down, get down (Look at me)<br />
Freak out, freak out, freak out, freak out<br />
Look at me now<br />
<br />
[Pre-Chorus]<br />
'Cause all I ever wanted was love<br />
Hey yeah, hey yeah (Ooh-ooh)<br />
Hey yeah, hey yeah (Ooh-ooh)<br />
Hey yeah, hey yeah<br />
All I ever wanted was love<br />
Hey yeah, hey yeah (Ooh-ooh)<br />
Hey yeah, hey yeah (Ooh-ooh)<br />
Hey yeah, hey yeah, hey yeah (Hey yeah, hey yeah)<br />
<br />
[Chorus]<br />
I want your stupid love, love<br />
I want your stupid love, love<br />
(Oh-oh-oh, oh-oh-oh, oh-oh, oh-oh-oh-oh-oh)<br />
<br />
[Bridge]<br />
I don't need a reason (Oh)<br />
Not sorry, I want your stupid love<br />
I don't need a reason (Oh)<br />
Not sorry, I want your stupid love<br />
Hey yeah, hey yeah<br />
<br />
[Chorus]<br />
I want your stupid love, love (Oh, oh, woo)<br />
We got a stupid love, love (Love, love, oh)<br />
(Oh-oh-oh, oh-oh-oh, oh-oh, oh-oh-oh-oh-oh)<br />
I want your stupid love, love<br />
(Oh-oh-oh, oh-oh-oh, oh-oh, oh-oh-oh-oh-oh)<br />
I want your stupid love, love"""
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
