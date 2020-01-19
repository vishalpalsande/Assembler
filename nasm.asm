section .data
	str1 db 10,3,4
	msg db "1 pass assembler done",10,0
	str2 db "vishal",10,0
	str3 db "PUCSD",10,0

section .bss
    n resd 1
    c resq 2
    d resb 1

section .text
    global main

main:
	mov eax, 10
	add eax, ebx
	mov ebx, 25
	mov eax, ebx
	mov eax, eax
	sub eax, ecx
lp1:	add eax, 10
	add ebx, 10
	sub ebx, 10
	sub edi, 20
	je lp1
	sub eax, 30
lp2:	mov eax, str1
	mov ecx, str2
	mov ebx, str3
	add eax, ecx
	jmp lp2
	
