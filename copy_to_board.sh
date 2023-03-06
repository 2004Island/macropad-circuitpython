#!/bin/sh
MACRO_PAD_PATH=/media/alex/CIRCUITPY
cp -r ./firmware/lib $MACRO_PAD_PATH/
cp ./code_1.py $MACRO_PAD_PATH/code.py
cp ./kdl/kdl.py $MACRO_PAD_PATH/kdl.py
cp ./kdl/mc_test.kdl $MACRO_PAD_PATH/test.kdl
cp ./LL_Honoka3_128x64.pbm $MACRO_PAD_PATH/LL_Honoka3_128x64.pbm
cp ./pbm_codec.py $MACRO_PAD_PATH/pbm_codec.py
cp ./firmware/font5x8.bin $MACRO_PAD_PATH/font5x8.bin
