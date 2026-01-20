public class BankWithLock {
    static int balance = 0;

    public synchronized void run() {
        balance += 100;
        System.out.println(
            "[LOCK] After deposit " +
            Thread.currentThread().getName() + " " +
            balance
        );

        balance -= 100;
        System.out.println(
            "[LOCK] After withdraw " +
            Thread.currentThread().getName() + " " +
            balance
        );
    }
}
