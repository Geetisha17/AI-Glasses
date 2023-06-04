import 'dart:io';
import 'package:http/http.dart' as http;
import 'dart:convert';

String uploadUrl = "http://192.168.43.232:5000/api";
String downloadUrl = "http://192.168.43.232:5000/result";

Future<dynamic> getData(String url) async {
  http.Response response = await http.get(Uri.parse(url));
  return jsonDecode(response.body);
}

Future<void> uploadImage(File imageFile, String url) async {
  String base64Image = base64Encode(imageFile.readAsBytesSync());
  http.Response response = await http.post(
    Uri.parse(url),
    body: base64Image,
    headers: {"Content-Type": "application/octet-stream"},
  );
  print(response.statusCode);
}

