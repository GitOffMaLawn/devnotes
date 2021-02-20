#NoEnv
#SingleInstance Force

mousedrag_threshold := 20 ; pixels

Hotkey mbutton, paste_selection

; #IfWinNotActive ahk_class ConsoleWindowClass

~lButton::
    MouseGetPos, mousedrag_x, mousedrag_y
    keywait lbutton, T0.3 
    If (ErrorLevel)
    {
        keywait lbutton
        mousegetpos, mousedrag_x2, mousedrag_y2
        if (abs(mousedrag_x2 - mousedrag_x) > mousedrag_threshold
        or abs(mousedrag_y2 - mousedrag_y) > mousedrag_threshold)
        {
            ; MouseGetPos,,,WindowUnderMouse
            ; WinGetClass, Class, ahk_id %WindowUnderMouse%
            ; If (Class != "ConsoleWindowClass")
                sendinput ^c
            hotkey mbutton, on
        }
    }
return

~lButton Up:: return

; #IfWinNotActive

paste_selection:

    if clipboard!=""
            {
            sendinput {lbutton}
            SendInput ^v
            Sleep, 200 ; Give some time for the text to be pasted.
            clipboard = ; clear the clipboard
            hotkey mbutton, off
            }

    return