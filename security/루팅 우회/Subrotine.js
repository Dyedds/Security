if(ObjC.available){

  try{

        var module_base = Module.findBaseAddress('');  //앱 Base명 입력

        var sub = module_base.add();   // 오프셋 값 입력
	
 

         Interceptor.attach(sub, {  

            onEnter: function (args) {

               

                console.log("");

                console.log("서브루틴 주소:" + sub);

                console.log("베이스주소:" + module_base);

                console.log("[+] 사용자함수 호출");

               

       

                console.log("args: " + args[2]+", "+args[3]+", "+args[4]+", "+args[5]+", "+args[6]);

            },

            onLeave: function (retval) {

                 console.log("\t[-] Type of return value: " + typeof retval);

            console.log("\t[-] Original Return Value: " + retval);

            retval.replace(0x0); // 리턴값 변환

            console.log("\t[-] Type of return value: " + typeof retval);

            console.log("\t[-] Return Value: " + retval);

           

            }

        });

    }

    catch(err){

        console.log("[!] Error: " + err.message);

    }

}

else {

    console.log("Objective-C Runtime is not available!");

}
