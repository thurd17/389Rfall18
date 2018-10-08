section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame
	mov rbx, rsi
	mov rcx, rdx
	mov r8, 0
lp:
	mov [rdi+ r8], bl
	add r8, 1
	loop lp
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame
	
	mov rcx,rdx
	mov r8, rbx	

copy_loop: 
	mov bl, byte [rsi + r8]
	mov byte [rdi + r8] , bl
	mov r8, rdx
	sub r8, rcx
	loop copy_loop 

	mov bl, byte [rsi + r8]
	mov byte [rdi + r8], bl
	mov r8, 0 
	leave 
	ret

