package com.company;

import java.text.NumberFormat;
import java.util.Scanner;

public class Mort {
    public static void main(String[] args) {
        System.out.print("Principle: ");
        Scanner Scanner = new Scanner(System.in);
        String principle = Scanner.nextLine();
        System.out.print("Annual Interest: ");
        String Annual = Scanner.nextLine();
        System.out.print("Peroid (Years)");
        String Years = Scanner.nextLine();

        var p = Float.parseFloat(principle);
        var i = Float.parseFloat(Annual);
        var n = (Float.parseFloat(Years)) * 12 ;
        var firstEquat = Math.pow(1 + i, n);

        var mort = (p *((i * firstEquat) /(firstEquat - 1 )));
        var round = Math.ceil(mort);
        NumberFormat percent = NumberFormat.getCurrencyInstance();

        System.out.print(percent.format(round));




    }






    }
