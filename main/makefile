DIR_INC = ./include
DIR_SRC = ./src
DIR_OBJ = ./obj
DIR_BIN = ./bin

cflags=-I/export/data/zjiaad/anaconda3/envs/ghash/include/python3.6m -I/export/data/zjiaad/anaconda3/envs/ghash/include/python3.6m  -Wno-unused-result -Wsign-compare -march=nocona -mtune=haswell -ftree-vectorize -fPIC -fstack-protector-strong -fno-plt -O3 -ffunction-sections -pipe -isystem /export/data/zjiaad/anaconda3/envs/ghash/include -fdebug-prefix-map=/home/builder/ktietz/cos6/ci_cos6/python_1622833237666/work=/usr/local/src/conda/python-3.6.13 -fdebug-prefix-map=/export/data/zjiaad/anaconda3/envs/ghash=/usr/local/src/conda-prefix -fuse-linker-plugin -ffat-lto-objects -flto-partition=none -flto -DNDEBUG -fwrapv -O3 -Wall
ldflags=-L/export/data/zjiaad/anaconda3/envs/ghash/lib/python3.6/config-3.6m-x86_64-linux-gnu -L/export/data/zjiaad/anaconda3/envs/ghash/lib -lpython3.6m -lpthread -ldl  -lutil -lm  -Xlinker -export-dynamic


SRC = $(wildcard ${DIR_SRC}/*.cpp)  
OBJ = $(patsubst %.cpp,${DIR_OBJ}/%.o,$(notdir ${SRC})) 

TARGET = main

BIN_TARGET = ${DIR_BIN}/${TARGET}

CC = g++
CFLAGS = -std=c++0x -g -Wall -I${DIR_INC} -L$(DIR_OBJ) -D_FILE_OFFSET_BITS=64 -D_LARGE_FILE 

${BIN_TARGET}:${OBJ} main.cpp
	$(CC) $(OBJ) main.cpp $(ldflags) $(cflags) $(CFLAGS) -o $@     

${DIR_BIN}/topK:${OBJ} topK.cpp
	$(CC) $(OBJ) topK.cpp $(ldflags) $(cflags) $(CFLAGS) -o $@     


${DIR_BIN}/test:${OBJ} test.cpp
	$(CC) $(OBJ) test.cpp $(ldflags) $(cflags) $(CFLAGS) -o $@     


${DIR_OBJ}/%.o:${DIR_SRC}/%.cpp
	$(CC) $(CFLAGS) -c  $<  $(ldflags) $(cflags) -o $@

clean:
	rm ${DIR_OBJ}/*.o bin/main bin/test
