#getVoltage:getVoltage.o
#	gcc getVoltage.c -o getVoltage -lbcm2835
#
# Simple .so Makefile
#
#\
CC		:= gcc	
#:= 覆盖之前的值\
LD		:= ld	\
CFLAGS	:=	\
LDFLAGS	:= -shared -fpic	\
#“$(wildcard *.c)”:获取工作目录下的所有的.c文件列表	\
SOURCE	:= $(wildcard *.c)	\
#patsubst把$(SOURCE)中的变量符合后缀是.c的全部替换成.o	\
OBJS	:= $(patsubst %.c,%.o,$(SOURCE))	\
TARGET_LIB := x.so	\
	\
all:$(OBJS)	\
	echo $(OBJS)	\
	$(LD) $(LDFLAGS) -o $(TARGET_LIB) $(OBJS)	\
	\
%.o:%.c	\
	@echo Compiling $< ...	\
	$(CC) -c $(CFLAGS)  $< -o $*.o	\
	\
.PHONY: clean	
#“.PHONY”表示，clean是个伪目标文件

#只有make cleam时起作用	\
clean:	\
    rm *.so *.o -rf

getVoltage.so:getVoltage.o
	gcc -o getVoltage.so -fPIC -shared getVoltage.o -lbcm2835
#gcc ads1256_test.c -o ads1256_test -lbcm2835
	
###	编译源文件
getVoltage.o:getVoltage.c
	gcc -c getVoltage.c

.PHONY: clean	
#“.PHONY”表示，clean是个伪目标文件	
clean:
	-rm *.out *.o *.bak
#--------------------- 
#作者：friendan 
#来源：CSDN 
#原文：https://blog.csdn.net/friendan/article/details/44702425 
#版权声明：本文为博主原创文章，转载请附上博文链接！