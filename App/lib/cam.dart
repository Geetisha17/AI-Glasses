import 'package:flutter/material.dart';
import './main.dart';
import 'package:ai_glasses/camera.dart';
import 'package:camera/camera.dart';
import 'dart:io';
import 'package:ai_glasses/face_detector_painter.dart';
import 'package:google_mlkit_commons/google_mlkit_commons.dart';
import 'package:google_mlkit_face_detection/google_mlkit_face_detection.dart';


class Cam extends StatefulWidget {
  const Cam({super.key});

  @override
  State<Cam> createState() => _CamState();
}

class _CamState extends State<Cam> {

  late CameraController controller;
  final FaceDetector _faceDetector = FaceDetector(
    options: FaceDetectorOptions(
      enableContours: true,
      enableClassification: true,
    ),
  );
  bool _canProcess = true;
  bool _isBusy = false;
  CustomPaint? _customPaint;
  String? _text;

  void initState() {
    super.initState();
    controller = CameraController(
      cameras[0],
      ResolutionPreset.max,
      imageFormatGroup: Platform.isAndroid
          ? ImageFormatGroup.nv21 // for Android
          : ImageFormatGroup.bgra8888,
    );
    controller.initialize().then((_) {
      if (!mounted) {
        return;
      }
      setState(() {});
    }).catchError((Object e) {
      if (e is CameraException) {
        switch (e.code) {
          case 'CameraAccessDenied':
            // Handle access errors here.
            break;
          default:
            // Handle other errors here.
            break;
        }
      }
    });
  }
    Future<void> processImage(InputImage inputImage) async {
    if (!_canProcess) return;
    if (_isBusy) return;
    _isBusy = true;
    setState(() {
      _text = '';
    });
    final faces = await _faceDetector.processImage(inputImage);
    if (inputImage.metadata?.size != null &&
        inputImage.metadata?.rotation != null) {
      final painter = FaceDetectorPainter(
          faces, inputImage.metadata!.size, inputImage.metadata!.rotation);
      _customPaint = CustomPaint(painter: painter);
    } else {
      String text = 'Faces found: ${faces.length}\n\n';
      for (final face in faces) {
        text += 'face: ${face.boundingBox}\n\n';
      }
      _text = text;
      // TODO: set _customPaint to draw boundingRect on top of image
      _customPaint = null;
    }
    _isBusy = false;
    if (mounted) {
      setState(() {});
    }
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: !controller.value.isInitialized
            ? Container()
            : CameraView(
                title: 'Face Detector',
                customPaint: _customPaint,
                text: _text,
                onImage: (inputImage) {
                  processImage(inputImage);
                },
                initialDirection: CameraLensDirection.front,
              ));
  }
}