
object Sample
{
    def main(args:Array[string])
    {
        var num:Int = 0;

        print("Enter number : ")
        num = scala.io.StdIn.readInt()

        if(num >= 0)
            println(num, " number is POSITIVE")
        else
            println(num, " number is NEGATIVE")
    }
}

///////////////////////////////////////////////////////

// for selecting folder :   cd Desktop/folder ch nav

// spark-shell   : to check scall is installed is not

// load program.scala

// Sample.main(Array())

///////////////////////////////////////////////////////