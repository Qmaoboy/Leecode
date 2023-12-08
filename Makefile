cc:=gcc


all:Two_sum.cc
	${cc} $^ -o $@

%.o:%.cc
	${cc} $*.cc -o $*.o

.PHONY:clean
clean:
	rm -rf *.o