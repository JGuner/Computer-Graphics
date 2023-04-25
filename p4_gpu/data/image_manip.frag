// Fragment shader
// The fragment shader is run once for every pixel
// It can change the color and transparency of the fragment.

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_TEXLIGHT_SHADER

// Set in Processing
uniform sampler2D my_texture;
uniform sampler2D my_mask;
uniform float blur_flag;

// These values come from the vertex shader
varying vec4 vertColor;
varying vec3 vertNormal;
varying vec3 vertLightDir;
varying vec4 vertTexCoord;

void main() { 

  // grab the color values from the texture and the mask
  vec4 diffuse_color = texture2D(my_texture, vertTexCoord.xy);
  vec4 mask_color = texture2D(my_mask, vertTexCoord.xy);
  int blurRadius = 0;
if(blur_flag == 1){

  if(mask_color.r < 0.1){
    blurRadius = 4;
    vec4 blurColor = vec4(0, 0, 0, 0);
    float texelSize = 1.0 / 768.0;
    for (int i = -blurRadius; i <= blurRadius; i++){
    for (int j = -blurRadius; j <= blurRadius; j++){
      vec2 temp = vec2(vertTexCoord.x + i*texelSize, vertTexCoord.y + j*texelSize);
      vec4 tempColor = texture2D(my_texture, temp);
      blurColor += tempColor;
      }
    }
    blurColor /= (2 * blurRadius) * (2 * blurRadius);
    // simple diffuse shading model
    float diffuse = clamp(dot (vertNormal, vertLightDir),0.0,1.0);
  
    gl_FragColor = vec4(blurColor.r, blurColor.g, blurColor.b, 1);
  }
  if((0.1 <= mask_color.r) && (mask_color.r <= 0.5)){
    blurRadius = 2;
    vec4 blurColor = vec4(0, 0, 0, 0);
      float texelSize = 1.0 / 768.0;
      for (int i = -blurRadius; i <= blurRadius; i++){
      for (int j = -blurRadius; j <= blurRadius; j++){
        vec2 temp = vec2(vertTexCoord.x + i*texelSize, vertTexCoord.y + j*texelSize);
        vec4 tempColor = texture2D(my_texture, temp);
        blurColor += tempColor;
        }
      }
      blurColor /= (2.5* blurRadius) * ( 2.5* blurRadius);
      // simple diffuse shading model
      float diffuse = clamp(dot (vertNormal, vertLightDir),0.0,1.0);
    
      gl_FragColor = vec4(blurColor.r, blurColor.g, blurColor.b, 1);
    }
  if(mask_color.r > 0.5){
          float diffuse = clamp(dot (vertNormal, vertLightDir),0.0,1.0);
          gl_FragColor = texture2D(my_texture, vertTexCoord.xy);
        }
}
else{
          float diffuse = clamp(dot (vertNormal, vertLightDir),0.0,1.0);
          gl_FragColor = texture2D(my_texture, vertTexCoord.xy);
}
}