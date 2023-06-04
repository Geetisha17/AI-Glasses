import 'package:ai_glasses/result.dart';
import 'package:flutter/material.dart';
import 'dart:io';
import 'package:image_picker/image_picker.dart';
import 'api.dart';
import 'package:fluttertoast/fluttertoast.dart';

class Home extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => HomeState();
}

class HomeState extends State<Home> {
  late File _image;

  Future getImage(bool isCamera) async {
    late File image;

    if (isCamera) {
      XFile? xFile = await ImagePicker().pickImage(source: ImageSource.camera);
      if (xFile != null) {
        image = File(xFile.path);
      }
    } else {
      XFile? xFile = await ImagePicker().pickImage(source: ImageSource.gallery);
      if (xFile != null) {
        image = File(xFile.path);
      }
    }
    uploadImage(image, uploadUrl);
    Fluttertoast.showToast(
  msg: "IMAGE UPLOADED !",
  toastLength: Toast.LENGTH_LONG,
  textColor: Colors.black,
  backgroundColor: Colors.white12,
  fontSize: 16.0,
  gravity: ToastGravity.BOTTOM,
);


    setState(() {
      _image = image;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        gradient: LinearGradient(
          begin: Alignment.topRight,
          end: Alignment.bottomLeft,
          stops: [0.1, 0.5, 0.7, 0.9],
          colors: [
            Colors.yellow[800]!,
            Colors.yellow[700]!,
            Colors.yellow[600]!,
            Colors.yellow[400]!,
          ],
        ),
      ),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        appBar: AppBar(
          backgroundColor: Colors.transparent,
          centerTitle: true,
          elevation: 0,
          title: Text(
            'Captioner',
            style: TextStyle(
                fontSize: 40, fontWeight: FontWeight.bold, color: Colors.black),
          ),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              IconButton(
                icon: Icon(Icons.insert_drive_file),
                color: Colors.white,
                iconSize: 70,
                onPressed: () {
                  getImage(false);
                },
              ),
              SizedBox(
                height: 70.0,
              ),
              IconButton(
                icon: Icon(Icons.camera_alt),
                color: Colors.white,
                iconSize: 70,
                onPressed: () {
                  getImage(true);
                },
              ),
              SizedBox(
                height: 70.0,
              ),
            ],
          ),
        ),
        floatingActionButton: FloatingActionButton.extended(
          onPressed: () {
            Navigator.push(
                context,
                MaterialPageRoute(
                    builder: (context) =>
                        ResultPage(key: UniqueKey(), image: _image)));
            ;
          },
          icon: Icon(
            Icons.arrow_forward,
            color: Colors.black,
            size: 30,
          ),
          label: Text(
            "Next",
            style: TextStyle(color: Colors.black, fontSize: 20),
          ),
          backgroundColor: Colors.white,
        ),
      ),
    );
  }
}
