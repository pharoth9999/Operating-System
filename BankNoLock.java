public class BankNoLock {
    static int balance = 0;

    public void run() {
        balance += 100;
        System.out.println(
            "[NO LOCK] After deposit " +
            Thread.currentThread().getName() + " " +
            balance
        );

        balance -= 100;
        System.out.println(
            "[NO LOCK] After withdraw " +
            Thread.currentThread().getName() + " " +
            balance
        );
    }
}
