#backgrounds
# zoombg

#character images
image Anaya silent:
  "anaya silent.png"
  xpos 1260
  xanchor 0
  ypos 108
  yanchor 0

image Professor silent:
  "Professor silent.png"
  xpos 660
  xanchor 0
  ypos 108
  yanchor 0

image Frank silent:
  "Frank silent.png"
  xpos 1260
  xanchor 0
  ypos 720
  yanchor 0

image Cameron silent:
  "Cameron silent.png"
  xpos 660
  xanchor 0
  ypos 414
  yanchor 0

image Iman silent:
  "iman silent.png"
  xpos 660
  xanchor 0
  ypos 720
  yanchor 0

image Paloma silent:
  "Paloma silent.png"
  xpos 60
  xanchor 0
  ypos 414
  yanchor 0

image Marcus silent:
  "Marcus silent.png"
  xpos 1260
  xanchor 0
  ypos 414
  yanchor 0 

image Demi silent:
  "demi silent.png"
  xpos 60
  xanchor 0
  ypos 720
  yanchor 0

image Anaya talking:
  "anaya talking.png"
  xpos 1260
  xanchor 0
  ypos 108
  yanchor 0

#player images
image playerwindowview:
   "playerwindowview.png"
   xpos 60
   xanchor 0
   ypos 108
   yanchor 0

#video links
image videolink = Text("{a=https://www.youtube.com/watch?v=5lbGAzo9RrM}https://youtu.be/5lbGAzo9RrM{/a}")

#blurred background
image zoomwindows_blurred = im.Blur ("bg zoomwindows.png", 1.5)

#window outlines for 9
image outline player:
   "windowoutline.png"
   xpos 54
   xanchor 0
   ypos 102
   yanchor 0

image outline Professor:
   "windowoutline.png"
   xpos 654
   xanchor 0
   ypos 102
   yanchor 0

image outline Anaya:
   "windowoutline.png"
   xpos 1254
   xanchor 0
   ypos 102
   yanchor 0

image outline Paloma:
   "windowoutline.png"
   xpos 54
   xanchor 0
   ypos 408
   yanchor 0

image outline Cameron:
   "windowoutline.png"
   xpos 654
   xanchor 0
   ypos 408
   yanchor 0

image outline Marcus:
   "windowoutline.png"
   xpos 1254
   xanchor 0
   ypos 408
   yanchor 0

image outline Demi:
   "windowoutline.png"
   xpos 54
   xanchor 0
   ypos 714
   yanchor 0

image outline Iman:
   "windowoutline.png"
   xpos 654
   xanchor 0
   ypos 714
   yanchor 0

image outline Frank:
   "windowoutline.png"
   xpos 1254
   xanchor 0
   ypos 714
   yanchor 0

#chatboxes
image chatbox everyone:
  "chatbox everyone.png"

image chatbox cameron:
  "chatbox cameron.png"

image chatbox cameron typing_i_like_you:
  "chatbox cameron typing_i_like_you.png"

image chatbox cameron i_like_you:
  "chatbox cameron i_like_you.png"

image chatbox cameron R_background:
  "chatbox cameron R_background.png"

image chatbox cameron haha_thanks:
  "chatbox cameron haha_thanks.png"

image chatbox cameron uh_thanks:
  "chatbox cameron uh_thanks.png"

image chatbox iman:
  "chatbox iman.png"

# mute icons
image mute_button unmute:
  "unmute.png"
  xpos 69
  xanchor 0
  ypos 355
  yanchor 0

image mute_button mute:
  "mute.png"
  xpos 61
  xanchor 0
  ypos 355
  yanchor 0

image mute_button unmute6:
  "unmute.png"
  xpos 69
  xanchor 0
  ypos 507
  yanchor 0

image mute_button mute6:
  "mute.png"
  xpos 50
  xanchor 0
  ypos 330
  yanchor 0

image mute_button mute3:
  "mute.png"
  xpos 50
  xanchor 0
  ypos 400
  yanchor 0

image mute_button unmute3:
  "unmute.png"
  xpos 69
  xanchor 0
  ypos 612
  yanchor 0

# incoming call image
image phone_call demi:
  "call.png"
  xpos 1424
  xanchor 0
  ypos 66
  yanchor 0

# facetime image
image facetime demi:
  "facetime.png"
  xpos 1380
  xanchor 0
  ypos 75
  yanchor 0

# demi's video off
image demi_video_off:
  "playerwindow.png"
  xpos 60
  xanchor 0
  ypos 718
  yanchor 0

#Demi's name when video is off
image demi = Text("Demi")

#small window outlines
image small_outline Player:
   "smallwindowoutline.png"
   xpos 1530
   xanchor 0
   ypos 62
   yanchor 0

image small_outline Professor:
   "smallwindowoutline.png"
   xpos 1530
   xanchor 0
   ypos 418
   yanchor 0

image small_outline Frank:
   "smallwindowoutline.png"
   xpos 1530
   xanchor 0
   ypos 240
   yanchor 0

image small_outline Paloma:
   "smallwindowoutline.png"
   xpos 1530
   xanchor 0
   ypos 418
   yanchor 0

image small_outline Cameron:
   "smallwindowoutline.png"
   xpos 1530
   xanchor 0
   ypos 596
   yanchor 0

image small_outline Marcus:
   "smallwindowoutline.png"
   xpos 1530
   xanchor 0
   ypos 240
   yanchor 0

image small_outline Demi:
   "smallwindowoutline.png"
   xpos 1530
   xanchor 0
   ypos 774
   yanchor 0

image small_outline Iman:
   "smallwindowoutline.png"
   xpos 1530
   xanchor 0
   ypos 240
   yanchor 0

#hitler video
image Nein = Movie(play="NEIN!.webm")

#blurred background
image zoomwindows_blurred = im.Blur("bg zoomwindows.png", 1.5)


#glitch animation
image Cameron glitch:
  "cameron_glitch1.png"
  xpos 660
  xanchor 0
  ypos 414
  yanchor 0
  pause .5
  "cameron_glitch2.png"
  xpos 660
  xanchor 0
  ypos 414
  yanchor 0
  pause .5
  "cameron_glitch3.png"
  xpos 660
  xanchor 0
  ypos 414
  yanchor 0
  pause .5
  repeat

#image Iman glitch:
#image Demi glitch:

#characters for 8
image Marcus silent8:
  "Marcus silent.png"
  xpos 360
  xanchor 0
  ypos 720
  yanchor 0

image Demi silent8:
  "Demi silent.png"
  xpos 1260
  xanchor 0
  ypos 414
  yanchor 0

image Iman silent8:
  "Iman silent.png"
  xpos 660
  xanchor 0
  ypos 414
  yanchor 0

image Frank silent8:
  "Frank silent.png"
  xpos 960
  xanchor 0
  ypos 720
  yanchor 0

#window outline for 8
image outline Marcus8:
   "windowoutline.png"
   xpos 436
   xanchor 0
   ypos 272
   yanchor 0

image outline Demi8:
   "windowoutline.png"
   xpos 836
   xanchor 0
   ypos 272
   yanchor 0

image outline Iman8:
   "windowoutline.png"
   xpos 237
   xanchor 0
   ypos 476
   yanchor 0

image outline Frank8:
   "windowoutline.png"
   xpos 637
   xanchor 0
   ypos 476
   yanchor 0

#window outline for 7
image outline Frank7:
   "windowoutline.png"
   xpos 437
   xanchor 0
   ypos 476
   yanchor 0

#characters for 7
image Demi silent7:
  "demi silent.png"
  xpos 660
  xanchor 0
  ypos 414
  yanchor 0

image Frank silent7:
  "Frank silent.png"
  xpos 660
  xanchor 0
  ypos 720
  yanchor 0

#characters for 6
image Professor silent6:
   "Professor silent.png"
   xpos 660
   xanchor 0
   ypos 260
   yanchor 0

image Anaya silent6:
   "Anaya silent.png"
   xpos 1260
   xanchor 0
   ypos 260
   yanchor 0

image Paloma silent6:
   "Paloma silent.png"
   xpos 60
   xanchor 0
   ypos 566
   yanchor 0

image Marcus silent6:
   "Marcus silent.png"
   xpos 660
   xanchor 0
   ypos 566
   yanchor 0

image Frank silent6:
   "Frank silent.png"
   xpos 1260
   xanchor 0
   ypos 566
   yanchor 0

#window outlines for 6
image outline player6:
   "windowoutline.png"
   xpos 54
   xanchor 0
   ypos 254
   yanchor 0

image outline Professor6:
   "windowoutline.png"
   xpos 654
   xanchor 0
   ypos 254
   yanchor 0

image outline Anaya6:
   "windowoutline.png"
   xpos 1254
   xanchor 0
   ypos 254
   yanchor 0

image outline Paloma6:
   "windowoutline.png"
   xpos 36
   xanchor 0
   ypos 374
   yanchor 0

image outline Marcus6:
   "windowoutline.png"
   xpos 436
   xanchor 0
   ypos 374
   yanchor 0

image outline Frank6:
   "windowoutline.png"
   xpos 836
   xanchor 0
   ypos 374
   yanchor 0


#facetime demi fade to black animation
image facetime fade:
  "facetime.png"
  "facetime_black.png" with dissolve

#window outlines for 3
image outline player3:
   "windowoutline.png"
   xpos 54
   xanchor 0
   ypos 360
   yanchor 0

image outline Anaya3:
   "windowoutline.png"
   xpos 654
   xanchor 0
   ypos 360
   yanchor 0


image outline Paloma3:
   "windowoutline.png"
   xpos 1254
   xanchor 0
   ypos 360
   yanchor 0

#characters for 3
image Paloma silent3:
   "Paloma silent.png"
   xpos 1260
   xanchor 0
   ypos 366
   yanchor 0

image Anaya silent3:
   "Anaya silent.png"
   xpos 660
   xanchor 0
   ypos 366
   yanchor 0

#screen shot images
#image Iman_screenshot:
#image Demi_screenshot:

#Anaya and Jerome alone
image Anaya silent2:
   "Anaya silent2.png"
   xpos 0
   xanchor 0
   ypos 203
   yanchor 0

image Jerome silent:
   "Jerome silent.png"
   xpos 581
   xanchor 0
   ypos 203
   yanchor 0