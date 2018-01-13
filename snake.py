import pygame
import sys
import random
import time


class Snake:
    def __init__(self):
        
        self.GameHeight=700
        
        self.GameWidth=1000

        self.SnakeParticleSize=20
        self.FoodSize=20
        
        pygame.init()
        
        self.GameDisplay=pygame.display.set_mode((self.GameWidth,self.GameHeight))
        
        pygame.display.set_caption("Snake Ninza")

        self.Clock=pygame.time.Clock()
        
        self.GameBoardImage=pygame.image.load("./snakeninza/welcome_game_board.png")
        self.SnakeHead=pygame.image.load("./snakeninza/head.png")
        self.SnakeBodyImage=pygame.image.load("./snakeninza/hbody.png")
        self.SnakeBendingImage=pygame.image.load("./snakeninza/bend.png")
        self.BlankBoardImage=pygame.image.load("./snakeninza/blank_gameboard2.jpg")

        self.SmallFont=pygame.font.SysFont("comicsansms",16)
        self.MediumFont=pygame.font.SysFont("comicsansms",35)
        self.LargeFont=pygame.font.SysFont("verdana",50)
        self.ExtraSmallFont=pygame.font.SysFont("Times New Roman",20)
        
        self.red=(255,0,0)
        self.grey=(211,211,211)
        self.blue=(0,0,255)
        self.green=(0,155,0)
        self.black=(0,0,0)
        self.purple=(128,0,128)
        self.yellow=(255,186,97)
        self.SnakeColor=(186,168,148)
        self.button_bgcolor=(124,96,46)
        self.white=(255,255,255)
        self.PlaySpaceColor=(87,174,47)
        self.ResultTextColor=(69,22,10)
        
        self.LevelsDetails=[]
        
        self.GameData={}
        
        self.GameStatus=None

        self.Start()
        #self.Obstacle()
    
    def ReadLevels(self):

        global LevelsDetails
        
        self.LevelsDetails=[]
        
        fp=open("./GameDatas/categories.txt","r")
        for line in fp:
            self.LevelsDetails.append([int(x) for x in list(line.split()[0])])  #   line.split() will return the list of string after removing "\n",tab,spaces in a string
                                                                                # here line.split()[0] means first element of the list returned by line.split()        i.e like ['010101']    
        fp.close()
        
    def UpdateLevels(self):
        
        global LevelsDetails
        
        levels=[]
               
        for i in self.LevelsDetails:
            levels.append([''.join([str(x) for x in i])])
        
        
        fp=open("./GameDatas/categories.txt","w")
        
        for i in levels:
            fp.write(i[0]+"\n")         #here levels is the list of lists of all stages in string format i.e [['010010']]
                                        # so iterator i[0] means 1st element of the first list of levels which is a string
        
        fp.close()
        
    def Start(self):

        global GameStatus
        global GameData
        global LevelsDetails
        
        Option=0
        Level=-1
        
        GameFlag=None
        start_ticks=0
        seconds=0
        
        while True:            
            Option=self.HomeScreen()
        
            if Option==0:                
                self.GameData["category"]="Easy"
                
            elif Option==1:
                self.GameData["category"]="Meduium"
            elif Option==2:
                self.GameData["catagory"]="Hard"
                
            Level=self.SelectLevels(Option)

            if Level==0:
                pass
            
            else:
            
                while True:
                    
                    if Level==1:
                        
                        self.GameData["level"]=Level

                        self.GameStatus=self.GameBody()                        
                        
                        if self.GameStatus==0:
                            
                            GameFlag=self.GameResult()
                            
                            if GameFlag==0:     # 0 means user pressed the home button
                                break
                            elif GameFlag==1:   # 1 means user pressed the replay button
                                pass
                            
                        elif self.GameStatus==1:
                            
                            if self.GameStatus==1:       
                                self.LevelsDetails[1][0]=1      # these lines unlock the first level of medium and hard category after completing the first level of easy category
                                self.LevelsDetails[2][0]=1

                            self.LevelsDetails[Option][Level]=1    # here this line unlock the next stage of the Option value Category

                            self.UpdateLevels()                        
                            
                            GameFlag=self.GameResult()
                            
                            if GameFlag==0:     # 0 means user pressed the home button
                                break
                            elif GameFlag==1:   # 1 means user pressed the replay button
                                pass
                            elif GameFlag==2:
                                Level=2
                                
                    elif Level==2:

                        self.GameData["level"]=Level

                        self.GameStatus=self.GameBody()  
                        
                     
    def HomeScreen(self):
        global GameBoardImage
        global PlayBoardImage
        global GameDisplay
        global Clock

        global GameWidth
        global GameHeight

        global yellow
        global button_bgcolor
        global white

        global black
        global purple
        

        button_height=24
        button_width=140
        button_xcoord=self.GameWidth/2+250
        button_ycoord=self.GameHeight/2

        MenuOptionSelect=-1

        
        self.GameDisplay.blit(self.GameBoardImage,[0,0])

        

        self.Text_On_Screen("Feed The Snake",self.purple,self.GameWidth/2,self.GameHeight/2-240,"large")    # here the coords are the center point of text rectangle
    
        self.Text_On_Screen("The objective of the game is to eat apples",self.black,self.GameWidth/2,self.GameHeight/2-80,"small")
        
        self.Text_On_Screen("The more apples you eat the longer you get",self.black,self.GameWidth/2,self.GameHeight/2-40,"small")

        self.Text_On_Screen("If you run into yourself, or the edges, you die!",self.black,self.GameWidth/2,self.GameHeight/2,"small")
        
        self.Text_On_Screen("Developed By",self.black,self.GameWidth/2-360,self.GameHeight/2+110,"small")

        self.Text_On_Screen("SONU KUMAR",self.black,self.GameWidth/2-360,self.GameHeight/2+150,"small")


        

        self.Button("Easy",self.yellow,self.button_bgcolor,button_xcoord,button_ycoord+14,button_width,button_height)    #text,fcolor,bcolor,xcoord,ycoord,width,height
        
        self.Button("Medium",self.yellow,self.button_bgcolor,button_xcoord,button_ycoord+65,button_width,button_height)
    
        self.Button("Hard",self.yellow,self.button_bgcolor,button_xcoord,button_ycoord+118,button_width,button_height)
    
        self.Button("Instruction",self.yellow,self.button_bgcolor,button_xcoord,button_ycoord+168,button_width,button_height)
    
        self.Button("Scores",self.yellow,self.button_bgcolor,button_xcoord,button_ycoord+224,button_width,button_height)

        
        while True:
            
            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                    self.CloseGame()
                elif event.type==pygame.MOUSEMOTION:
                    
                    if (button_xcoord<= event.pos[0] <=button_xcoord+button_width) and (button_ycoord+14<= event.pos[1] <=button_ycoord+14+button_height):
                            
                        self.Button("Easy",self.white,self.button_bgcolor,button_xcoord,button_ycoord+14,button_width,button_height)
                    else:
                        self.Button("Easy",self.yellow,self.button_bgcolor,button_xcoord,button_ycoord+14,button_width,button_height)

                    if (button_xcoord<= event.pos[0] <=button_xcoord+button_width) and (button_ycoord+65<= event.pos[1] <=button_ycoord+65+button_height):
                            
                        self.Button("Medium",self.white,self.button_bgcolor,button_xcoord,button_ycoord+65,button_width,button_height)
                    else:
                        self.Button("Medium",self.yellow,self.button_bgcolor,button_xcoord,button_ycoord+65,button_width,button_height)

                    if (button_xcoord<= event.pos[0] <=button_xcoord+button_width) and (button_ycoord+118<= event.pos[1] <=button_ycoord+118+button_height):
                            
                        self.Button("Hard",self.white,self.button_bgcolor,button_xcoord,button_ycoord+118,button_width,button_height)
                    else:
                        self.Button("Hard",self.yellow,self.button_bgcolor,button_xcoord,button_ycoord+118,button_width,button_height)

                    if (button_xcoord<= event.pos[0] <=button_xcoord+button_width) and (button_ycoord+168<= event.pos[1] <=button_ycoord+168+button_height):
                            
                        self.Button("Instruction",self.white,self.button_bgcolor,button_xcoord,button_ycoord+168,button_width,button_height)
                    else:
                        self.Button("Instruction",self.yellow,self.button_bgcolor,button_xcoord,button_ycoord+168,button_width,button_height)

                    if (button_xcoord<= event.pos[0] <=button_xcoord+button_width) and (button_ycoord+224<= event.pos[1] <=button_ycoord+224+button_height):
                            
                        self.Button("Scores",self.white,self.button_bgcolor,button_xcoord,button_ycoord+224,button_width,button_height)
                    else:
                        self.Button("Scores",self.yellow,self.button_bgcolor,button_xcoord,button_ycoord+224,button_width,button_height)

                elif event.type==pygame.MOUSEBUTTONUP:
                    if event.button==1:
                        if (button_xcoord<= event.pos[0] <=button_xcoord+button_width) and (button_ycoord+14<= event.pos[1] <=button_ycoord+14+button_height):
                            MenuOptionSelect=0
                        if (button_xcoord<= event.pos[0] <=button_xcoord+button_width) and (button_ycoord+65<= event.pos[1] <=button_ycoord+65+button_height):
                            MenuOptionSelect=1
                        if (button_xcoord<= event.pos[0] <=button_xcoord+button_width) and (button_ycoord+118<= event.pos[1] <=button_ycoord+118+button_height):
                            MenuOptionSelect=2                                    

            if MenuOptionSelect!=-1:
                break
            pygame.display.update()
            self.Clock.tick(80)
            
        return MenuOptionSelect

    def Button(self,text_on_button,fg_col,bg_col,x_coord,y_coord,width,height):
        
        global GameDisplay
        
        pygame.draw.rect(self.GameDisplay,bg_col,(x_coord,y_coord,width,height))
    
        self.Text_On_Screen(text_on_button,fg_col,x_coord+width/2,y_coord+height/2,"small")   #here x_coord+width/2,y_coord+height/2 keeps the text rectangle in center of draw_rect

    

        
        
    def DrawSnake(self,SnakeList):
       
        global GameDisplay
        
        global SnakeBodyImage
        global SnakeBendingImage
        global SnakeHead
        
        for coord in SnakeList[:-1]:
            if coord[2]=="left" or coord[2]=="right":
                self.GameDisplay.blit(pygame.transform.rotate(self.SnakeBodyImage,0),[coord[0],coord[1]])

            elif coord[2]=="up" or coord[2]=="down":
                self.GameDisplay.blit(pygame.transform.rotate(self.SnakeBodyImage,90),[coord[0],coord[1]])
            
            elif coord[2]=="rightup" or coord[2]=="downleft":
                self.GameDisplay.blit(pygame.transform.rotate(self.SnakeBendingImage,0),[coord[0],coord[1]])
                                             
            elif coord[2]=="upleft" or coord[2]=="rightdown":
                self.GameDisplay.blit(pygame.transform.rotate(self.SnakeBendingImage,90),[coord[0],coord[1]])
                
            elif coord[2]=="leftdown" or coord[2]=="upright":
                self.GameDisplay.blit(pygame.transform.rotate(self.SnakeBendingImage,180),[coord[0],coord[1]])
                                             
            elif coord[2]=="downright" or coord[2]=="leftup":
                self.GameDisplay.blit(pygame.transform.rotate(self.SnakeBendingImage,270),[coord[0],coord[1]])

        if SnakeList[-1][2]=="left":
            head=pygame.transform.rotate(self.SnakeHead,90)
        
        
        elif SnakeList[-1][2]=="right":
            head=pygame.transform.rotate(self.SnakeHead,270)
            
            
        elif SnakeList[-1][2]=="up":
            head=pygame.transform.rotate(self.SnakeHead,0)
            
            
        elif SnakeList[-1][2]=="down":
            head=pygame.transform.rotate(self.SnakeHead,180)
            
            
        self.GameDisplay.blit(head,[SnakeList[-1][0],SnakeList[-1][1]])
            
        
            
    def GamePause(self):
        flag=1
        while flag:                
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.CloseGame()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        flag=0
                    else:
                        pass

    def Create_Text_Surface(self,msg,fcolor,font):

        if font=="exsmall":
            TextSurface=self.ExtraSmallFont.render(msg,True,fcolor)
        elif font=="small":
            TextSurface=self.SmallFont.render(msg,True,fcolor)
        elif font=="medium":
            TextSurface=self.MediumFont.render(msg,True,fcolor)
        elif font=="large":
            TextSurface=self.LargeFont.render(msg,True,fcolor)  
        
        return TextSurface

    def Text_On_Screen(self,msg,fcolor,Xpos,Ypos,font):

        TextSurface=self.Create_Text_Surface(msg,fcolor,font)
        
        TextRect=TextSurface.get_rect()

        TextRect.center=Xpos,Ypos-2
        
        self.GameDisplay.blit(TextSurface,TextRect)


            
    def SelectLevels(self,Option):
        global GameDisplay
        global Clock
        global PlayBoardImage
        global PlaySpaceColor
        global LevelsDetails

        PlaySpaceHeight=580
        PlaySpaceWidth=860

        PlaySpace_Xcoord=65
        PlaySpace_Ycoord=60

        PlaySpaceHeight=580
        PlaySpaceWidth=860
        
        LevelNumber = -1
        Back_Button_Hover=0
        Level_Hover_No=0

        Stages=None

        HoverBoxColor=(128,245,246)
        
        Lbanner=pygame.image.load("./snakeninza/level_banner.png")
        
        LockedLevel=pygame.image.load("./snakeninza/locked_level.png")
        
        BackNormalButton=pygame.image.load("./snakeninza/back_button_normal.jpg")
        BackActiveButton=pygame.image.load("./snakeninza/back_button_selected.jpg")

        self.ReadLevels()        

        self.GameDisplay.blit(self.BlankBoardImage,[0,0])

        pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[PlaySpace_Xcoord,PlaySpace_Ycoord,PlaySpaceWidth+1,PlaySpaceHeight+1]) # Filling the Play space with green
        pygame.draw.rect(self.GameDisplay,(0,0,0),[PlaySpace_Xcoord,PlaySpace_Ycoord,PlaySpaceWidth+1,PlaySpaceHeight+1],1)
        
        self.GameDisplay.blit(Lbanner,[PlaySpace_Xcoord+(PlaySpaceWidth-465)/2,PlaySpace_Ycoord+20]) #here 465 is the witdh of image

        Stages=self.LevelsDetails[Option]
            
        if Stages[0]==0:
                self.GameDisplay.blit(LockedLevel,[PlaySpace_Xcoord+220,PlaySpace_Ycoord+200])
        else:
            self.GameDisplay.blit(pygame.image.load("./snakeninza/opened_level1.png"),[PlaySpace_Xcoord+220,PlaySpace_Ycoord+200])
            
        if Stages[1]==0:
            self.GameDisplay.blit(LockedLevel,[PlaySpace_Xcoord+400,PlaySpace_Ycoord+200])
        else:
            self.GameDisplay.blit(pygame.image.load("./snakeninza/opened_level2.png"),[PlaySpace_Xcoord+400,PlaySpace_Ycoord+200])

        if Stages[2]==0:
            self.GameDisplay.blit(LockedLevel,[PlaySpace_Xcoord+580,PlaySpace_Ycoord+200])
        else:
            self.GameDisplay.blit(pygame.image.load("./snakeninza/opened_level3.png"),[PlaySpace_Xcoord+580,PlaySpace_Ycoord+200])

        if Stages[3]==0:
            self.GameDisplay.blit(LockedLevel,[PlaySpace_Xcoord+220,PlaySpace_Ycoord+380])
        else:
            self.GameDisplay.blit(pygame.image.load("./snakeninza/opened_level4.png"),[PlaySpace_Xcoord+220,PlaySpace_Ycoord+380])

        if Stages[4]==0:
            self.GameDisplay.blit(LockedLevel,[PlaySpace_Xcoord+400,PlaySpace_Ycoord+380])
        else:
            self.GameDisplay.blit(pygame.image.load("./snakeninza/opened_level5.png"),[PlaySpace_Xcoord+400,PlaySpace_Ycoord+380])

        if Stages[5]==0:
            self.GameDisplay.blit(LockedLevel,[PlaySpace_Xcoord+580,PlaySpace_Ycoord+380])
        else:
            self.GameDisplay.blit(pygame.image.load("./snakeninza/opened_level6.png"),[PlaySpace_Xcoord+580,PlaySpace_Ycoord+380])
            

        self.GameDisplay.blit(BackNormalButton,[PlaySpace_Xcoord+1,PlaySpace_Ycoord+545])
        
        
        while True:
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        self.CloseGame()
                        
                    elif event.type==pygame.MOUSEMOTION:
                        
                        if PlaySpace_Xcoord+1 <= event.pos[0] <= PlaySpace_Xcoord+1+70 and PlaySpace_Ycoord+545 <= event.pos[1] <= PlaySpace_Ycoord+545+35:
                            pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[PlaySpace_Xcoord+1,PlaySpace_Ycoord+545,70,35])                            
                            self.GameDisplay.blit(BackActiveButton,[PlaySpace_Xcoord+1,PlaySpace_Ycoord+545])
                            Back_Button_Hover=1
                        else:
                            if Back_Button_Hover==1:
                                pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[PlaySpace_Xcoord+1,PlaySpace_Ycoord+545,70,35])
                                self.GameDisplay.blit(BackNormalButton,[PlaySpace_Xcoord+1,PlaySpace_Ycoord+545])
                                Back_Button_Hover=0
                                
                        if (PlaySpace_Xcoord+220 <= event.pos[0] <= PlaySpace_Xcoord+220+80) and (PlaySpace_Ycoord+200 <= event.pos[1] <= PlaySpace_Ycoord+200+80):
                            pygame.draw.rect(self.GameDisplay,HoverBoxColor,[PlaySpace_Xcoord+218,PlaySpace_Ycoord+198,82,82],2)
                            Level_Hover_No=1
                        else:
                            if Level_Hover_No==1:
                                pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[PlaySpace_Xcoord+218,PlaySpace_Ycoord+198,82,82],2)
                                Level_Hover_No=0
                                
                        if (PlaySpace_Xcoord+400 <= event.pos[0] <= PlaySpace_Xcoord+400+80) and (PlaySpace_Ycoord+200 <= event.pos[1] <= PlaySpace_Ycoord+200+80):
                            pygame.draw.rect(self.GameDisplay,HoverBoxColor,[PlaySpace_Xcoord+398,PlaySpace_Ycoord+198,82,82],2)
                            Level_Hover_No=2
                        else:                            
                            if Level_Hover_No==2:
                                pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[PlaySpace_Xcoord+398,PlaySpace_Ycoord+198,82,82],2)
                                Level_Hover_No=0

                        if (PlaySpace_Xcoord+580 <= event.pos[0] <= PlaySpace_Xcoord+580+80) and (PlaySpace_Ycoord+200 <= event.pos[1] <= PlaySpace_Ycoord+200+80):
                            pygame.draw.rect(self.GameDisplay,HoverBoxColor,[PlaySpace_Xcoord+578,PlaySpace_Ycoord+198,82,82],2)
                            Level_Hover_No=3
                        else:                            
                            if Level_Hover_No==3:
                                pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[PlaySpace_Xcoord+578,PlaySpace_Ycoord+198,82,82],2)
                                Level_Hover_No=0

                        if (PlaySpace_Xcoord+220 <= event.pos[0] <= PlaySpace_Xcoord+220+80) and (PlaySpace_Ycoord+380 <= event.pos[1] <= PlaySpace_Ycoord+380+80):
                            pygame.draw.rect(self.GameDisplay,HoverBoxColor,[PlaySpace_Xcoord+218,PlaySpace_Ycoord+378,82,82],2)
                            Level_Hover_No=4
                        else:
                            if Level_Hover_No==4:
                                pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[PlaySpace_Xcoord+218,PlaySpace_Ycoord+378,82,82],2)
                                Level_Hover_No=0

                        if (PlaySpace_Xcoord+400 <= event.pos[0] <= PlaySpace_Xcoord+400+80) and (PlaySpace_Ycoord+380 <= event.pos[1] <= PlaySpace_Ycoord+380+80):
                            pygame.draw.rect(self.GameDisplay,HoverBoxColor,[PlaySpace_Xcoord+398,PlaySpace_Ycoord+378,82,82],2)
                            Level_Hover_No=5
                        else:
                            if Level_Hover_No==5:
                                pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[PlaySpace_Xcoord+398,PlaySpace_Ycoord+378,82,82],2)
                                Level_Hover_No=0
                                
                        if (PlaySpace_Xcoord+580 <= event.pos[0] <= PlaySpace_Xcoord+580+80) and (PlaySpace_Ycoord+380 <= event.pos[1] <= PlaySpace_Ycoord+380+80):
                            pygame.draw.rect(self.GameDisplay,HoverBoxColor,[PlaySpace_Xcoord+578,PlaySpace_Ycoord+378,82,82],2)
                            Level_Hover_No=6
                        else:
                            if Level_Hover_No==6:
                                pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[PlaySpace_Xcoord+578,PlaySpace_Ycoord+378,82,82],2)
                                Level_Hover_No=0
                                
                    elif event.type==pygame.MOUSEBUTTONUP:
                        if event.button==1:
                            
                            if PlaySpace_Xcoord+220 <= event.pos[0] <= PlaySpace_Xcoord+220+80 and PlaySpace_Ycoord+200 <= event.pos[1] <= PlaySpace_Ycoord+200+80:     # here 80 is width and height of the image of levels
                                if Stages[0]==1:
                                    LevelNumber=1
                                else:
                                    pass
                            if (PlaySpace_Xcoord+400 <= event.pos[0] <= PlaySpace_Xcoord+400+80) and (PlaySpace_Ycoord+200 <= event.pos[1] <= PlaySpace_Ycoord+200+80):
                                if Stages[1]==1:
                                    LevelNumber=2
                                else:
                                    pass
                            if (PlaySpace_Xcoord+580 <= event.pos[0] <= PlaySpace_Xcoord+580+80) and (PlaySpace_Ycoord+200 <= event.pos[1] <= PlaySpace_Ycoord+200+80):
                                if Stages[2]==1:
                                    Levelnumber=3
                                else:
                                    pass
                            if (PlaySpace_Xcoord+220 <= event.pos[0] <= PlaySpace_Xcoord+220+80) and (PlaySpace_Ycoord+380 <= event.pos[1] <= PlaySpace_Ycoord+380+80):
                                if Stages[3]==1:
                                    LevelNumber=4
                                else:
                                    pass

                            if (PlaySpace_Xcoord+400 <= event.pos[0] <= PlaySpace_Xcoord+400+80) and (PlaySpace_Ycoord+380 <= event.pos[1] <= PlaySpace_Ycoord+380+80):
                                if Stages[4]==1:
                                    LevelNumber=5
                                else:
                                    pass

                            if (PlaySpace_Xcoord+580 <= event.pos[0] <= PlaySpace_Xcoord+580+80) and (PlaySpace_Ycoord+380 <= event.pos[1] <= PlaySpace_Ycoord+380+80):
                                if Stages[5]==1:
                                    LevelNumber=6
                                else:
                                    pass
                            
                            if PlaySpace_Xcoord+1 <= event.pos[0] <= PlaySpace_Xcoord+1+70 and PlaySpace_Ycoord+545 <= event.pos[1] <= PlaySpace_Ycoord+545+35:  # here +70 is width and +35 is the height of the image of backbutton
                                LevelNumber=0
                                

            if LevelNumber != -1:
                break
            else:
                self.Clock.tick(80)
                pygame.display.update()
                
        return LevelNumber
    
    def Obstacle(self):

        global BlankBoardImage
        global Clock
        global SnakeParticleSize
        
        PlaySpace_Xcoord=65
        PlaySpace_Ycoord=60

        PlaySpaceHeight=580
        PlaySpaceWidth=860

        obstacle1=pygame.image.load("./snakeninza/secondobst.png")
        obstacle2=pygame.image.load("./snakeninza/midtrunk.png")
        
        self.GameDisplay.blit(self.BlankBoardImage,[0,0])
        pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[PlaySpace_Xcoord,PlaySpace_Ycoord,PlaySpaceWidth+1,PlaySpaceHeight+1]) # Filling the Play space with green
        pygame.draw.rect(self.GameDisplay,(0,0,0),[PlaySpace_Xcoord,PlaySpace_Ycoord,PlaySpaceWidth+1,PlaySpaceHeight+1],1)
        

#------------------Easy->Stage-2--------------------------------------------------------------------------------------------------
        '''
        self.GameDisplay.blit(pygame.image.load("./snakeninza/midtrunk.png"),[PlaySpace_Xcoord+61,PlaySpace_Ycoord+61])
        
        x=681
        
        for i in range(3):
            self.GameDisplay.blit(pygame.image.load("./snakeninza/secondobst.png"),[PlaySpace_Xcoord+x,PlaySpace_Ycoord+61])
            x=x+40

        x=81
        
        for i in range(3):
            self.GameDisplay.blit(pygame.image.load("./snakeninza/secondobst.png"),[PlaySpace_Xcoord+x,PlaySpace_Ycoord+421])
            x=x+40
                
        self.GameDisplay.blit(pygame.transform.rotate(pygame.image.load("./snakeninza/midtrunk.png"),90),[PlaySpace_Xcoord+681,PlaySpace_Ycoord+481])
        '''
#------------------Easy->Stage-3----------------------------------------------------------------------------------------------------
        '''
        x=121
        
        for i in range(3):
            self.GameDisplay.blit(pygame.image.load("./snakeninza/secondobst.png"),[PlaySpace_Xcoord+x,PlaySpace_Ycoord+21])
            x=x+40

        x=21
        
        for i in range(3):
            self.GameDisplay.blit(pygame.image.load("./snakeninza/secondobst.png"),[PlaySpace_Xcoord+x,PlaySpace_Ycoord+141])
            x=x+40

        
        self.GameDisplay.blit(pygame.image.load("./snakeninza/midtrunk.png"),[PlaySpace_Xcoord+PlaySpaceWidth-181,PlaySpace_Ycoord+PlaySpaceHeight-121])
        self.GameDisplay.blit(pygame.transform.rotate(pygame.image.load("./snakeninza/midtrunk.png"),90),[PlaySpace_Xcoord+PlaySpaceWidth-121,PlaySpace_Ycoord+PlaySpaceHeight-141])
        '''
#------------------Easy->Stage-4---------------------------------------------------------------------------------------------------------        
        '''
        x=121
        
        for i in range(3):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+x,PlaySpace_Ycoord+21])
            x=x+40

        x=21
        
        for i in range(3):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+x,PlaySpace_Ycoord+141])
            x=x+40

        x=PlaySpaceWidth-241

        for i in range(3):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+x,PlaySpace_Ycoord+21])
            x=x+40

        x=PlaySpaceWidth-141

        for i in range(3):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+x,PlaySpace_Ycoord+141])
            x=x+40
        '''
#-----------------Easy-Stage-5-----------------------------------------------------------------------------------------------------        
        '''

        x=121
        
        for i in range(3):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+x,PlaySpace_Ycoord+21])
            x=x+40

        x=21
        
        for i in range(3):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+x,PlaySpace_Ycoord+141])
            x=x+40

        x=PlaySpaceWidth-241

        for i in range(3):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+x,PlaySpace_Ycoord+21])
            x=x+40

        x=PlaySpaceWidth-141

        for i in range(3):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+x,PlaySpace_Ycoord+141])
            x=x+40

        self.GameDisplay.blit(pygame.transform.rotate(obstacle2,270),[PlaySpace_Xcoord+21,PlaySpace_Ycoord+PlaySpaceHeight-141])    
        self.GameDisplay.blit(obstacle2,[PlaySpace_Xcoord+141,PlaySpace_Ycoord+PlaySpaceHeight-121])
        

        
        self.GameDisplay.blit(obstacle2,[PlaySpace_Xcoord+PlaySpaceWidth-181,PlaySpace_Ycoord+PlaySpaceHeight-121])
        self.GameDisplay.blit(pygame.transform.rotate(obstacle2,90),[PlaySpace_Xcoord+PlaySpaceWidth-121,PlaySpace_Ycoord+PlaySpaceHeight-141])

        '''

#--------------------Easy->Stage-6--------------------------------------------------------------------------------------
        '''
        x=121
        
        for i in range(3):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+x,PlaySpace_Ycoord+21])
            x=x+40

        x=21
        
        for i in range(3):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+x,PlaySpace_Ycoord+141])
            x=x+40

        x=PlaySpaceWidth-241

        for i in range(3):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+x,PlaySpace_Ycoord+21])
            x=x+40

        x=PlaySpaceWidth-141

        for i in range(3):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+x,PlaySpace_Ycoord+141])
            x=x+40

        self.GameDisplay.blit(pygame.transform.rotate(obstacle2,270),[PlaySpace_Xcoord+21,PlaySpace_Ycoord+PlaySpaceHeight-141])    
        self.GameDisplay.blit(obstacle2,[PlaySpace_Xcoord+141,PlaySpace_Ycoord+PlaySpaceHeight-121])
        

        
        self.GameDisplay.blit(obstacle2,[PlaySpace_Xcoord+PlaySpaceWidth-181,PlaySpace_Ycoord+PlaySpaceHeight-121])
        self.GameDisplay.blit(pygame.transform.rotate(obstacle2,90),[PlaySpace_Xcoord+PlaySpaceWidth-121,PlaySpace_Ycoord+PlaySpaceHeight-141])
        
        x=361
        y=221
        
        for i in range(3):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+x,PlaySpace_Ycoord+y])
            x=x+40

        '''
#----------------------------------------------------------------------------------------------------------------------------------------

        y=151

        for i in range(3):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+101,PlaySpace_Ycoord+y])
            y+=120

        x=181
    
        for i in range(6):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+x,PlaySpace_Ycoord+201])
            x+=80

        x=201
    
        for i in range(6):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+x,PlaySpace_Ycoord+321])
            x+=80

        y=151

        for i in range(3):
            self.GameDisplay.blit(obstacle1,[PlaySpace_Xcoord+701,PlaySpace_Ycoord+y])
            y+=120

        
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.CloseGame()

            
            pygame.display.update()
            self.Clock.tick(20)
        
    def GameBody(self):
        
        global SnakeParticleSize
        global BlankBoardImage
        global Clock
        global FoodSize
        global PlayBoardImage
        global PlaySpaceColor
        global GameData
        
        
        PlaySpaceHeight=580
        PlaySpaceWidth=860

        PlaySpace_Xcoord=65
        PlaySpace_Ycoord=60
        
        SnakeList=[]
        SnakeLength=1
        Bend=0
        
        NextDirection="right"
        PrevDirection="right"

        x_incr=0
        y_incr=0

        FoodX=0
        FoodY=0

        UpFlag=0
        DownFlag=0
        
        LeftFlag=0        
        RightFlag=0

        PlayTimeFlag=0
        PlayStartTime=0
        PlayEndTime=0
        TotalSeconds=0
        
        FoodFlag=0            
        
        spd=20
        fps=10

        hr=0
        mn=0
        sec=0


        Total_Apple_Eaten=0

        Remaining_Apples_Coords=[]

        Each_Apple_Strength=0

        GameStatus=None

        apple=pygame.image.load("./snakeninza/apple.png")

        self.GameDisplay.blit(self.BlankBoardImage,[0,0])
        
        FoodX=random.randrange(PlaySpace_Xcoord+1,PlaySpace_Xcoord+PlaySpaceWidth+1,self.SnakeParticleSize)
        FoodY=random.randrange(PlaySpace_Ycoord+1,PlaySpace_Ycoord+PlaySpaceHeight+1,self.SnakeParticleSize)

        SnakeX=random.randrange(PlaySpace_Xcoord+1, PlaySpace_Xcoord+PlaySpaceWidth+1, self.SnakeParticleSize)
        SnakeY=random.randrange(PlaySpace_Ycoord+1, PlaySpace_Ycoord+PlaySpaceHeight+1, self.SnakeParticleSize)
        
        pygame.draw.rect(self.GameDisplay,(0,0,0),[PlaySpace_Xcoord,PlaySpace_Ycoord,PlaySpaceWidth+1,PlaySpaceHeight+1],1)

        
       # pygame.draw.rect(self.GameDisplay,(0,0,0),[PlaySpace_Xcoord+PlaySpaceWidth+3,PlaySpace_Ycoord+68,24,295],1)
       
        x=0
        y=0
        
        x=PlaySpace_Xcoord+PlaySpaceWidth+5
        y=PlaySpace_Ycoord+70
        
        for i in range(10):
            self.GameDisplay.blit(apple,[x,y])
            Remaining_Apples_Coords.append([x,y])
            y+=30

        if self.GameData["category"]=="Easy":
            Each_Apple_Strength=1
        elif self.GameData["category"]=="Medium":
            Each_Apple_Strength=8
        elif self.GameData["category"]=="Hard":
            Each_Apple_Strength=5


        self.GameData["total_apple"]=Each_Apple_Strength*10
        
        
        while True:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.CloseGame()

                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                            self.GamePause()
  
                    if event.key==pygame.K_LEFT:
                        if RightFlag==1 or LeftFlag==1:
                            pass
                        else:                            
                            x_incr=-spd
                            y_incr=0
                            
                            UpFlag=0
                            DownFlag=0

                            NextDirection="left"
                            
                            LeftFlag=1
                            RightFlag=1
                            
                            Bend=1

                            if PlayTimeFlag==0:
                                PlayTimeFlag=1     # to start timer
                                PlayStartTime=pygame.time.get_ticks()
                            
                    elif event.key==pygame.K_RIGHT:
                        if LeftFlag==1 or RightFlag==1:
                            pass
                        else:
                            x_incr=spd
                            y_incr=0

                            UpFlag=0
                            DownFlag=0
                            
                            NextDirection="right"

                            LeftFlag=1
                            RightFlag=1

                            Bend=1
                            
                            if PlayTimeFlag==0:
                                PlayTimeFlag=1
                                PlayStartTime=pygame.time.get_ticks()
                            
                    elif event.key==pygame.K_UP:
                        if DownFlag==1 or UpFlag==1:
                            pass
                        else:
                            y_incr=-spd
                            x_incr=0

                            LeftFlag=0
                            RightFlag=0
                            
                            NextDirection="up"
                            
                            UpFlag=1
                            DownFlag=1

                            Bend=1
                            
                            if PlayTimeFlag==0:
                                PlayTimeFlag=1
                                PlayStartTime=pygame.time.get_ticks()
                            
                    elif event.key==pygame.K_DOWN:
                        if UpFlag==1 or DownFlag==1:
                            pass
                        else:
                            y_incr=spd
                            x_incr=0

                            LeftFlag=0
                            RightFlag=0
                            
                            NextDirection="down"
                            
                            DownFlag=1
                            UpFlag=1

                            Bend=1
                            
                            if PlayTimeFlag==0:
                                PlayTimeFlag=1
                                PlayStartTime=pygame.time.get_ticks()
                            
            SnakeX=SnakeX+x_incr
            SnakeY=SnakeY+y_incr
                
            if len(Remaining_Apples_Coords)==0:
                
                PlayEndTime=pygame.time.get_ticks()
                
                GameStatus=1

                self.CalculateGameData(PlayStartTime,PlayEndTime,Total_Apple_Eaten)
                
            elif SnakeX < PlaySpace_Xcoord+1 or SnakeX+self.SnakeParticleSize > PlaySpace_Xcoord + PlaySpaceWidth + 1 or SnakeY < PlaySpace_Ycoord+1 or SnakeY+self.SnakeParticleSize > PlaySpace_Ycoord+PlaySpaceHeight+1:

                PlayEndTime=pygame.time.get_ticks()
                
                GameStatus=0

                self.CalculateGameData(PlayStartTime,PlayEndTime,Total_Apple_Eaten)
                
                break
            else:
                if (SnakeX+self.SnakeParticleSize>FoodX and SnakeX+self.SnakeParticleSize<FoodX+self.FoodSize) or (SnakeX<FoodX+self.FoodSize and SnakeX+self.SnakeParticleSize>FoodX):
                    if (SnakeY+self.SnakeParticleSize>FoodY and SnakeY+self.SnakeParticleSize<FoodY+self.FoodSize) or (SnakeY<FoodY+self.FoodSize and SnakeY+self.SnakeParticleSize>FoodY):
                        
                        SnakeLength+=1
                        Total_Apple_Eaten+=1
                        
                        if Total_Apple_Eaten % Each_Apple_Strength == 0 and SnakeLength!=1:   # In first  iteration 0%6 will be zero, so to avoid it the SnakeLength is used
                            pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[Remaining_Apples_Coords[0][0],Remaining_Apples_Coords[0][1],20,20])
                            
                            del Remaining_Apples_Coords[0]      #it removes the top most apple from the screen after each 10 apples eaten
                            
                        FoodX=random.randrange(PlaySpace_Xcoord+1,PlaySpace_Xcoord+PlaySpaceWidth+1,self.SnakeParticleSize)
                        FoodY=random.randrange(PlaySpace_Ycoord+1,PlaySpace_Ycoord+PlaySpaceHeight+1,self.SnakeParticleSize)

                SnakeHead=[]
                SnakeHead.append(SnakeX)
                SnakeHead.append(SnakeY)

                SnakeHead.append(NextDirection)

                if Bend==1:
                    SnakeList[-1][2]=PrevDirection+NextDirection            # changing the direction value at bending place
                    
                    PrevDirection=NextDirection
                    Bend=0

                SnakeList.append(SnakeHead)
                
                if len(SnakeList)>SnakeLength:
                    del SnakeList[0]
                    
                for EachCord in SnakeList[:-1]:             #Ignoring the just appended element
                    if (EachCord[0]==SnakeList[-1][0]) and (EachCord[1]==SnakeList[-1][1]):         #this check if snake run in itself
                        GameStatus=0
                        break
                if GameStatus==0:
                    
                    PlayEndTime=pygame.time.get_ticks()
                
                    GameStatus=0

                    self.CalculateGameData(PlayStartTime,PlayEndTime,Total_Apple_Eaten)
                    
                else:
                    pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[PlaySpace_Xcoord,PlaySpace_Ycoord,PlaySpaceWidth+1,PlaySpaceHeight+1]) # Filling the Play space with green
                    pygame.draw.rect(self.GameDisplay,(0,0,0),[PlaySpace_Xcoord,PlaySpace_Ycoord,PlaySpaceWidth+1,PlaySpaceHeight+1],1) # drawing Playing Box here width=1
                    
                    self.GameDisplay.blit(apple,[FoodX,FoodY])

                    self.DrawSnake(SnakeList)
                   # self.Obstacle()
                    pygame.display.update()
                    self.Clock.tick(fps)
            if GameStatus==0 or GameStatus==1:
                break
        return GameStatus


    def CalculateGameData(self,PlayStartTime,PlayEndTime,Total_Apple_Eaten):

        global GameData

        hr=0
        mn=0
        TotalSeconds=0
        
        self.GameData["total_apple_eaten"]=Total_Apple_Eaten

        TotalSeconds=(PlayEndTime-PlayStartTime)/1000

        hr=TotalSeconds/3600
        TotalSeconds=TotalSeconds%3600
        
        mn=TotalSeconds/60
        TotalSeconds=TotalSeconds%60

        
        self.GameData["time_taken"]=str(hr)+" : "+str(mn)+" : "+str(TotalSeconds)

        
        
    def GameResult(self):
        
        global BlankBoardImage
        global PlaySpaceColor
        global ResultTextColor
        global yellow
        global GameData

        PlaySpaceHeight=580
        PlaySpaceWidth=860
        
        PlaySpace_Xcoord=65
        PlaySpace_Ycoord=60

        GameFlag=-1
        
        Home_Button_Hover=None
        Replay_Button_Hover=None
        Next_Button_Hover=None

        Inactive_Home_Button_Image=pygame.image.load("./snakeninza/inactive_home.png")
        Active_Home_Button_Image=pygame.image.load("./snakeninza/active_home.png")
        
        Inactive_Replay_Button_Image=pygame.image.load("./snakeninza/inactive_playagain.png")
        Active_Replay_Button_Image=pygame.image.load("./snakeninza/active_playagain.png")
        

        self.GameDisplay.blit(self.BlankBoardImage,[0,0])
        
        pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[PlaySpace_Xcoord,PlaySpace_Ycoord,PlaySpaceWidth+1,PlaySpaceHeight+1])
        pygame.draw.rect(self.GameDisplay,(0,0,0),[PlaySpace_Xcoord,PlaySpace_Ycoord,PlaySpaceWidth+1,PlaySpaceHeight+1],1)

        
        self.GameDisplay.blit(pygame.image.load("./snakeninza/levelresultboard.jpg"),[(PlaySpaceWidth-480)/2+PlaySpace_Xcoord,(PlaySpaceHeight-350)/2+PlaySpace_Ycoord+40])        
        
        self.Text_On_Screen(self.GameData["category"],self.ResultTextColor,(PlaySpaceWidth-480)/2+PlaySpace_Xcoord+360,(PlaySpaceHeight-350)/2+PlaySpace_Ycoord+40+45,"exsmall")
        self.Text_On_Screen(str(self.GameData["level"]),self.ResultTextColor,(PlaySpaceWidth-480)/2+PlaySpace_Xcoord+360,(PlaySpaceHeight-350)/2+PlaySpace_Ycoord+40+85,"exsmall")
        self.Text_On_Screen(str(self.GameData["total_apple"]),self.ResultTextColor,(PlaySpaceWidth-480)/2+PlaySpace_Xcoord+360,(PlaySpaceHeight-350)/2+PlaySpace_Ycoord+40+120,"exsmall")
        self.Text_On_Screen(str(self.GameData["total_apple_eaten"]),self.ResultTextColor,(PlaySpaceWidth-480)/2+PlaySpace_Xcoord+360,(PlaySpaceHeight-350)/2+PlaySpace_Ycoord+40+160,"exsmall")
        self.Text_On_Screen(str(self.GameData["time_taken"]),self.ResultTextColor,(PlaySpaceWidth-480)/2+PlaySpace_Xcoord+360,(PlaySpaceHeight-350)/2+PlaySpace_Ycoord+40+200,"exsmall")
        self.Text_On_Screen(str(self.GameData["total_apple_eaten"]*5),self.ResultTextColor,(PlaySpaceWidth-480)/2+PlaySpace_Xcoord+360,(PlaySpaceHeight-350)/2+PlaySpace_Ycoord+40+235,"exsmall")

        if self.GameStatus==0:
            self.GameDisplay.blit(pygame.image.load("./snakeninza/levelgameover.png"),[((PlaySpaceWidth-640)/2)+PlaySpace_Xcoord,PlaySpace_Ycoord+20])
            self.Text_On_Screen("UnCleared",self.ResultTextColor,(PlaySpaceWidth-480)/2+PlaySpace_Xcoord+360,(PlaySpaceHeight-350)/2+PlaySpace_Ycoord+40+270,"exsmall")

            
        elif self.GameStatus==1:
            
            self.GameDisplay.blit(pygame.image.load("./snakeninza/levelcompleted.png"),[(PlaySpaceWidth-610)/2+PlaySpace_Xcoord,PlaySpace_Ycoord+20])
            self.Text_On_Screen("Cleared",self.ResultTextColor,(PlaySpaceWidth-480)/2+PlaySpace_Xcoord+360,(PlaySpaceHeight-350)/2+PlaySpace_Ycoord+40+270,"exsmall")
            self.GameDisplay.blit(pygame.image.load("./snakeninza/deactivenext.png"),[(PlaySpaceWidth-70)/2+PlaySpace_Xcoord,PlaySpace_Ycoord+520])          
            
        self.GameDisplay.blit(Inactive_Home_Button_Image,[(PlaySpaceWidth-480)/2+PlaySpace_Xcoord,PlaySpace_Ycoord+520])                
        self.GameDisplay.blit(Inactive_Replay_Button_Image,[PlaySpace_Xcoord+120+480,PlaySpace_Ycoord+520])
       
        
               
        
        while 1:    
            for event in pygame.event.get():
        
                if event.type==pygame.QUIT:
                    self.CloseGame()
                elif event.type==pygame.MOUSEMOTION:
        
                    if ((PlaySpaceWidth-480)/2+PlaySpace_Xcoord <= event.pos[0] <= (PlaySpaceWidth-480)/2+PlaySpace_Xcoord+70) and (PlaySpace_Ycoord+520 <=event.pos[1] <= PlaySpace_Xcoord+520+35):
                        pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[(PlaySpaceWidth-480)/2+PlaySpace_Xcoord,PlaySpace_Ycoord+520,70,35])
                        self.GameDisplay.blit(Active_Home_Button_Image,[(PlaySpaceWidth-480)/2+PlaySpace_Xcoord,PlaySpace_Ycoord+520])
                        Home_Button_Hover=True
                    else:
                        if Home_Button_Hover==True:
                            pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[(PlaySpaceWidth-480)/2+PlaySpace_Xcoord,PlaySpace_Ycoord+520,70,35])
                            self.GameDisplay.blit(Inactive_Home_Button_Image,[(PlaySpaceWidth-480)/2+PlaySpace_Xcoord,PlaySpace_Ycoord+520])
                            Home_Button_Hover=False    
                        
                        
                    if (PlaySpace_Xcoord+120+480 <= event.pos[0] <= PlaySpace_Xcoord+120+480+70) and (PlaySpace_Ycoord+520 <= event.pos[1] <= PlaySpace_Ycoord+520+35):
                        pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[PlaySpace_Xcoord+120+480,PlaySpace_Ycoord+520,70,35])
                        self.GameDisplay.blit(Active_Replay_Button_Image,[PlaySpace_Xcoord+120+480,PlaySpace_Ycoord+520])
                        Replay_Button_Hover=True
                    else:
                        if Replay_Button_Hover==True:
                            pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[PlaySpace_Xcoord+120+480,PlaySpace_Ycoord+520,70,35])
                            self.GameDisplay.blit(Inactive_Replay_Button_Image,[PlaySpace_Xcoord+120+480,PlaySpace_Ycoord+520])
                            Replay_Button_Hover=False
                            
                    if self.GameStatus==1:
                        if ((PlaySpaceWidth-70)/2+PlaySpace_Xcoord <= event.pos[0] <= (PlaySpaceWidth-70)/2+PlaySpace_Xcoord+70) and (PlaySpace_Ycoord+520 <= event.pos[1] <= PlaySpace_Ycoord+520+35):
                            pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[(PlaySpaceWidth-70)/2+PlaySpace_Xcoord,PlaySpace_Ycoord+520,70,35])
                            self.GameDisplay.blit(pygame.image.load("./snakeninza/activenext.png"),[(PlaySpaceWidth-70)/2+PlaySpace_Xcoord,PlaySpace_Ycoord+520])
                            Next_Button_Hover=True
                        else:
                            if Next_Button_Hover==True:
                                pygame.draw.rect(self.GameDisplay,self.PlaySpaceColor,[(PlaySpaceWidth-70)/2+PlaySpace_Xcoord,PlaySpace_Ycoord+520,70,35])
                                self.GameDisplay.blit(pygame.image.load("./snakeninza/deactivenext.png"),[(PlaySpaceWidth-70)/2+PlaySpace_Xcoord,PlaySpace_Ycoord+520])
                                Next_Button_Hover=False
                    else:
                        pass
                elif event.type==pygame.MOUSEBUTTONUP:
                    if ((PlaySpaceWidth-480)/2+PlaySpace_Xcoord <= event.pos[0] <= (PlaySpaceWidth-480)/2+PlaySpace_Xcoord+70) and (PlaySpace_Ycoord+520 <=event.pos[1] <= PlaySpace_Xcoord+520+35):
                        GameFlag=0
                    if (PlaySpace_Xcoord+120+480 <= event.pos[0] <= PlaySpace_Xcoord+120+480+70) and (PlaySpace_Ycoord+520 <= event.pos[1] <= PlaySpace_Ycoord+520+35):
                        GameFlag=1

                        
            if GameFlag==0 or GameFlag==1:
                break
            else:                        
                pygame.display.update()
                self.Clock.tick(30)
                
        return GameFlag

    def CloseGame(self):
        pygame.quit()
        sys.exit()

        '''
        obstacle=pygame.image.load("./snakeninza/obs_particle.jpg")
        obstacle=pygame.image.load("./snakeninza/big_obst.jpg")
        long_obstacle=pygame.image.load("./snakeninza/long_obst.jpg")
        self.GameDisplay.blit(obstacle,[PlaySpace_Xcoord+1+80,PlaySpace_Ycoord+1+80])
        self.GameDisplay.blit(long_obstacle,[PlaySpace_Xcoord+1+500,PlaySpace_Ycoord+1+400])        
        '''

        
if __name__=='__main__':
    MyGame=Snake()
