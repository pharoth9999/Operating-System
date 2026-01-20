public class Main {

    public static void main(String[] args) throws InterruptedException {

        System.out.println("===== WITHOUT LOCK =====");
        BankNoLock bank1 = new BankNoLock();
        runThreads(bank1);

        System.out.println("\n===== WITH LOCK =====");
        BankWithLock bank2 = new BankWithLock();
        runThreads(bank2);
    }

    static void runThreads(Object bank) throws InterruptedException {

        Runnable task;

        if (bank instanceof BankNoLock) {
            task = ((BankNoLock) bank)::run;
        } else {
            task = ((BankWithLock) bank)::run;
        }

        Thread t1 = new Thread(task, "Thread1");
        Thread t2 = new Thread(task, "Thread2");
        Thread t3 = new Thread(task, "Thread3");

        t1.start();
        t2.start();
        t3.start();

        t1.join();
        t2.join();
        t3.join();
    }
}
