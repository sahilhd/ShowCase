package emailapp;

import java.util.Scanner;

public class Email {

    private String firstName;
    private String lastName;
    private String password;
    private String department;
    private int mailBoxCap = 500;
    private String email;
    private int passLen = 10;
    private String alternateEmail;
    private String companySuf = "company.com";


    public Email(String firstName , String lastName) { // creating login
        this.firstName = firstName;
        this.lastName = lastName;
        System.out.println("Email Created : " + this.firstName + " " + this.lastName);

        this.department = setDepartment();
        System.out.println("Department:" + this.department);
        this.password = RandomPass(passLen);
        System.out.println("PassWord:" + this.password);

        email = firstName.toLowerCase() + "." + lastName.toLowerCase() + "@" + department + "." + companySuf;
        System.out.println("Your email:" + email);
    }

    private String setDepartment() {
        System.out.print(" Enter the Department: \n1 for SALES \n2 for DEVELOPMENT \n3 for ACCOUNTING \n0 for none ");
        Scanner in = new Scanner(System.in);
        int depChoice = in.nextInt();

        if (depChoice == 1) {
            return "SALES";
        }
        else if (depChoice ==2) {
            return "DEVELOPMENT";
        }
        else if (depChoice == 3) {
            return "Accounting";
        }
        else
            return "";
    }
    private String RandomPass(int length) {
        String passwordSetup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$";
        char [] password = new char [length];
        for (int a = 0; a < length; a++) {
            int rand =  (int) (Math.random() * passwordSetup.length());
            password[a] = passwordSetup.charAt(rand);
        }
        return new String (password);
    }
    public void mailBoxCap (int capacity) {
        this.mailBoxCap = capacity;
    }
    public void altEmail(String alternateEmail) {
        this.alternateEmail = alternateEmail
    }
    public void changePassword(String password) {
        this.password = password;
    }
    public int getMailBoxCap() {return getMailBoxCap();}
    public String getAlternateEmail() { return getAlternateEmail;}
    public String getPassword() { return password;}

}
