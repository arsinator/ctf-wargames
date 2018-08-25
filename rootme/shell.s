.data


.text

.global main


main:
xor %eax,%eax
push %eax
mov $0x0000000b,%eax
mov $0x0068732f, %ecx
push %ecx
mov $0x706d742f , %ecx
push %ecx
mov %esp,%ebx
xor %ecx,%ecx
push %ecx
push %ecx
push %ecx
xor %edx,%edx
mov %ebx,(%esp)
int $0x80
