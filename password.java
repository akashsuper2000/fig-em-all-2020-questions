import java.util.*;

class Function {
    public static void main(String args[]) {
        Function password = new Function();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the password: ");
        String userInput = scanner.next();
	if (password.checkPassword(userInput)) {
	    System.out.println("Access granted!");
	} else {
	    System.out.println("Access denied!");
        }
    }

    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            0x2c, 0x65, 0x20, 0xa,
            0x22, 0x65, 0x64, 0x31, 
            0xa, 0x3d, 0x34, 0x23, 
            0x66, 0xa, 0x31, 0x30, 
            0x33, 0x64, 0x3b, 0x64, 
            0x21, 0x30, 0x39, 0x2c, 
            0xa, 0x36, 0x3d, 0x30, 
            0x34, 0x62, 0x66, 0x31
        };
        for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
        }
        return true;
    }
}
