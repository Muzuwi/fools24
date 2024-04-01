#!/usr/bin/env bash

rgbasm ../res/gbhttp.asm -o gbhttp.o
rgblink -o gbhttp.gb -n gbhttp.sym gbhttp.o 
rgbfix -v gbhttp.gb

