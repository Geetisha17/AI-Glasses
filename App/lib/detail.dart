import 'package:flutter/material.dart';

class DetailPage extends StatelessWidget {
  const DetailPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Stack(
          children: [
            Column(
              children: [
                SizedBox(
                    height: 190,
                    ),
                Container(
                  margin: const EdgeInsets.only(top:100.0),
                  height: 120,
                  child: ListView(
                    scrollDirection: Axis.horizontal,
                    shrinkWrap: true,
                    children: [
                      Container(
                        margin: const EdgeInsets.all(20.0),
                        width: 120,
                        child: ClipRRect(
                            borderRadius: BorderRadius.circular(8.0),
                            ),
                      )                     
                    ],
                  ),
                ),
                Container(
                  margin:const EdgeInsets.symmetric(horizontal: 30.0,vertical: 30.0),
                  child:const Text("AI Glasses, also known as smart glasses or augmented reality glasses, are wearable devices that integrate artificial intelligence and advanced technologies to provide users with an enhanced and interactive experience. These glasses combine the functionality of traditional eyewear with cutting-edge features that leverage computer vision, machine learning, and augmented reality (AR) capabilities",style: TextStyle(
                    color: Colors.black38,
                    letterSpacing: 0.8,
                    height: 1.5,
      

                  ),),
              
                ),
              ],
            ),
            SafeArea(child: IconButton(onPressed: (){
              Navigator.pop(context);
            }, icon: const  Icon(Icons.arrow_back_rounded))),
            const Positioned(
                top: 100,
                left: 20,
                child: Text("Ai \nGlasses",style: TextStyle(
                  fontWeight: FontWeight.w500,
                  fontSize: 45
                ),))
          ],
        ),
      ),
    );
  }
}