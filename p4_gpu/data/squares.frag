// Fragment shader

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_LIGHT_SHADER

// These values come from the vertex shader
varying vec4 vertColor;
varying vec3 vertNormal;
varying vec3 vertLightDir;
varying vec4 vertTexCoord;

void main() { 
  gl_FragColor = vec4(0.2, 0.4, 1.0, 1);
  vec2 center = vec2(0.5, 0.2);
  mat2 rotationMatrix = mat2(
  cos(radians(45)), sin(radians(45)),   // first column
  -sin(radians(45)), cos(radians(45)));  // second column

  vec2 tempCoord = vec2(vertTexCoord);
  tempCoord.x = tempCoord.x + 0.20;
  tempCoord.y = tempCoord.y - 0.5;
  tempCoord = rotationMatrix * tempCoord;

  if (distance(tempCoord.x, center.x) <= 0.05) {
    if (distance(tempCoord.y, center.y) <= 0.05) {
        gl_FragColor.a = 0;
    }
  }
  for (int i = 0; i < 4; i++){
    center.y += 0.15;
    if (distance(tempCoord.x, center.x) <= 0.05) {
    if (distance(tempCoord.y, center.y) <= 0.05) {
      gl_FragColor.a = 0;
    }
    }
    if (i == 0 || i == 2){
    vec2 t1 = center;
    vec2 t2 = center;
    t1 = rotationMatrix * center;
      t1.x = center.x - 0.15;
      t2.x = center.x + 0.15;
    if (distance(tempCoord.x, t1.x) <= 0.05) {
    if (distance(tempCoord.y, center.y) <= 0.05) {
      gl_FragColor.a = 0;
    }
    }
    if (distance(tempCoord.x, t2.x) <= 0.05) {
    if (distance(tempCoord.y, center.y) <= 0.05) {
      gl_FragColor.a = 0;
  }
  }
}
  if (i == 1){
    vec2 t1 = vec2(center);
    vec2 t2 = vec2(center);
    vec2 t3 = vec2(center);
    vec2 t4 = vec2(center);
    t1.x = center.x - 0.15;
    t2.x = center.x + 0.15;
    t3.x = center.x - 0.30;
    t4.x = center.x + 0.30;

    if (distance(tempCoord.x, t1.x) <= 0.05) {
    if (distance(tempCoord.y, center.y) <= 0.05) {
      gl_FragColor.a = 0;
    }
    }
    if (distance(tempCoord.x, t2.x) <= 0.05) {
    if (distance(tempCoord.y, center.y) <= 0.05) {
      gl_FragColor.a = 0;
  }
  }
  if (distance(tempCoord.x, t3.x) <= 0.05) {
    if (distance(tempCoord.y, center.y) <= 0.05) {
      gl_FragColor.a = 0;
    }
    }
    if (distance(tempCoord.x, t4.x) <= 0.05) {
    if (distance(tempCoord.y, center.y) <= 0.05) {
      gl_FragColor.a = 0;
    }
    }
}
}

}
