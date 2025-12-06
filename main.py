@namespace
class SpriteKind:
    pokémaitre = SpriteKind.create()
    mechant_allie = SpriteKind.create()

def on_overlap_tile(sprite, location):
    mySprite.set_position(77, 120)
    tiles.set_current_tilemap(tilemap("""
        niveau
        """))
    scene.camera_follow_sprite(mySprite)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile4
        """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    global mySprite2
    scene.camera_follow_sprite(mySprite)
    mySprite2 = sprites.create(assets.image("""
            stevve0
            """),
        SpriteKind.mechant_allie)
    tiles.set_current_tilemap(tilemap("""
        niveau
        """))
    mySprite.set_position(62, 112)
    mySprite2.set_position(59, 112)
    mySprite2.set_velocity(-30, 0)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile3
        """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    global mySprite2
    mySprite.start_effect(effects.fire)
    music.stop_all_sounds()
    music.play(music.create_sound_effect(WaveShape.SINE,
            169,
            169,
            255,
            255,
            5000,
            SoundExpressionEffect.TREMOLO,
            InterpolationCurve.CURVE),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    mySprite.set_position(32, 28)
    tiles.set_current_tilemap(tilemap("""
        niveau2
        """))
    scene.camera_follow_sprite(mySprite)
    mySprite2 = sprites.create(assets.image("""
            stevve0
            """),
        SpriteKind.mechant_allie)
    mySprite2.set_position(127, 94)
    effects.clear_particles(mySprite)
    mySprite2.say_text("c'est l'heure de la vengance!", 2000, True)
    
    def on_after():
        mySprite.say_text("quoi !!", 2000, True)
        
        def on_after2():
            mySprite2.say_text("hein! qui est la ?", 2000, True)
            
            def on_after3():
                mySprite2.say_text("peut importe de toute facon l'odre de la pierre sera bientot hors de nuire ! ",
                    2000,
                    True)
                mySprite2.set_velocity(80, 50)
                tiles.set_current_tilemap(tilemap("""
                    niveau2
                    """))
                
                def on_after4():
                    tiles.set_current_tilemap(tilemap("""
                        niveau9
                        """))
                    
                    def on_after5():
                        global witherstormencharge
                        tiles.set_current_tilemap(tilemap("""
                            niveau11
                            """))
                        witherstormencharge = sprites.create(img("""
                        .............fffffff.............
                        ..........ffccccccccccff.........
                        .......ffccccccccccccccccff......
                        .....fccccccccffffffffccccccf....
                        ....fccccccfffff4444fffffcccf....
                        ...fcccccfcccff444444ffcccccff...
                        ..fcccccccccff444444ffccccccccf..
                        ..fccccccccccf444444fcccccccccf..
                        ..fcccccccccff444444ffccccccccf..
                        ...fcccccfcccff4444ffcccccccff...
                        ....fccccccfffff44fffffcccccff...
                        .....fccccccccffffffffccccccf....
                        .......ffccccccccccccccccff......
                        ..........ffccccccccccff.........
                        ............fffccccfff...........
                        .............ffccccff............
                        ..............fcccf..............
                        ..............fccf...............
                        ...............fff...............
   """),
                            SpriteKind.player)
                    timer.after(2000, on_after5)
                    
                timer.after(2000, on_after4)
                
            timer.after(2000, on_after3)
            
        timer.after(2000, on_after2)
        
    timer.after(2000, on_after)
    
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        base wither storm
        """),
    on_overlap_tile3)

def on_overlap_tile4(sprite4, location4):
    sprites.destroy(mySprite2)
    game.show_long_text("au voleur! reviens ici !!!", DialogLayout.BOTTOM)
    mySprite.set_position(59, 112)
    mySprite.set_velocity(-50, 0)
scene.on_overlap_tile(SpriteKind.mechant_allie,
    assets.tile("""
        base wither storm
        """),
    on_overlap_tile4)

witherstormencharge: Sprite = None
mySprite2: Sprite = None
mySprite: Sprite = None
music.play(music.create_song(hex("""
        0078000408020106001c00010a006400f401640000040000000000000000000000000000000002660000000400012404000800012408000c0001240c001000012210001400012014001800012018001c0001201c002000021e20200024000222252400280002242528002c0001242c0030000222243000340002222434003800012538003c0001243c004000022425
        """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
tiles.set_current_tilemap(tilemap("""
    niveau1
    """))
mySprite = sprites.create(assets.image("""
    stevve
    """), SpriteKind.player)
mySprite.set_position(76, 109)
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
game.show_long_text("allons au village nous trouverons peut etre quelque chose d'interrésant !",
    DialogLayout.BOTTOM)
tiles2 = 0

def on_forever():
    pass
forever(on_forever)
