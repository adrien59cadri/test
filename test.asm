         org 7C00h
 
         jmp short Start ;Jump over the data (the 'short' keyword makes the jmp instruction smaller)
 
 HelloMsg:    db 'Hello World! ' , 0
 RamMsg:      db 'RAM size is : ',0
 
 Start:  xor dx, dx      ;Start at top left corner cursor
         mov ds, dx       ;Ensure ds = org (to let us load the message)
                         ;note the message adress is DS:SI, ie sector ds:offest si
         call PrintHello
         call GoToLine
         call PrintRam
         retn

GoToLine:
         inc dh
         xor dl,dl
         cmp dh, 25
         jne EndGTL
         xor dh,dh
EndGTL:  retn

PrintHello:
         mov si, HelloMsg     ;Loads the address of the first byte of the message, 7C02h in this case
         call Print
         retn
         
PrintRam:
         mov si,RamMsg
         call Print
         xor ax, ax                      ; clear ax
         int 0x12                        ; get the amount of KB from the BIOS
         retn
 
 Print:  mov bx, 000Fh   ;Page 0, colour attribute 15 (white) for the int 10 calls below
         mov cx, 1       ;We will want to write 1 character
         cld             ;Ensure direction flag is cleared (for LODSB) -> the cursors goes from left to right
 
                         ;PC BIOS Interrupt 10 Subfunction 2 - Set cursor position
                         ;AH = 2
 Char:   mov ah, 2       ;BH = page, DH = row, DL = column
         int 10h
         mov al, [si]
         inc si
                         ;PC BIOS Interrupt 10 Subfunction 9 - Write character and colour
                         ;AH = 9
         mov ah, 9       ;BH = page, AL = character, BL = attribute, CX = character count
         int 10h
 
         inc dl          ;Advance cursor
 
         cmp dl, 80      ;Wrap around edge of screen if necessary
         jne Skip
         xor dl, dl
         inc dh
 
         cmp dh, 25      ;Wrap around bottom of screen if necessary
         jne Skip
         xor dh, dh
Skip: 
         or al,al
         jnz Char        ;continue loading characters
         retn
 
 
 times 0200h - 2 - ($ - $$)  db 0    ;Zerofill up to 510 bytes
 
         dw 0AA55h       ;Boot Sector signature