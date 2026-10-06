#define cube_x       = 40
#define cube_y       = 80
#define cube_size    = 50
#define cube_color_r = 101
#define cube_color_g = 154
#define cube_color_b = 210

void c_power(void *buffer, int w) {
    unsigned char *pixels = (unsigned char*)buffer;

    // calculo: (yw + x) * 3 + canal
    for (int i=cube_y; i < cube_y+cube_size; i++) {
        for (int j=cube_x; j < cube_x+cube_size; j++) {
            pixels[(i*w + j) * 3 + 0] = cube_color_r;
            pixels[(i*w + j) * 3 + 1] = cube_color_g;
            pixels[(i*w + j) * 3 + 2] = cube_color_b;
        }
    }
}
// Você pode compilar com:
// gcc -shared -fPIC test.c -o test.o
