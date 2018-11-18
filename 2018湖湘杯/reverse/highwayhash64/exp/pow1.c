#include "highwayhash.h"

#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>

#define kMaxSize 64

static const uint64_t kTestKey1[4] = {
  0x0706050403020100ull, 0x0F0E0D0C0B0A0908ull,
  0x1716151413121110ull, 0x1F1E1D1C1B1A1918ull
};

static const uint64_t kTestKey2[4] = {
  1ull, 2ull, 3ull, 4ull
};

const uint64_t kExpected64[kMaxSize + 1] = {
    0x907A56DE22C26E53ull, 0x7EAB43AAC7CDDD78ull, 0xB8D0569AB0B53D62ull,
    0x5C6BEFAB8A463D80ull, 0xF205A46893007EDAull, 0x2B8A1668E4A94541ull,
    0xBD4CCC325BEFCA6Full, 0x4D02AE1738F59482ull, 0xE1205108E55F3171ull,
    0x32D2644EC77A1584ull, 0xF6E10ACDB103A90Bull, 0xC3BBF4615B415C15ull,
    0x243CC2040063FA9Cull, 0xA89A58CE65E641FFull, 0x24B031A348455A23ull,
    0x40793F86A449F33Bull, 0xCFAB3489F97EB832ull, 0x19FE67D2C8C5C0E2ull,
    0x04DD90A69C565CC2ull, 0x75D9518E2371C504ull, 0x38AD9B1141D3DD16ull,
    0x0264432CCD8A70E0ull, 0xA9DB5A6288683390ull, 0xD7B05492003F028Cull,
    0x205F615AEA59E51Eull, 0xEEE0C89621052884ull, 0x1BFC1A93A7284F4Full,
    0x512175B5B70DA91Dull, 0xF71F8976A0A2C639ull, 0xAE093FEF1F84E3E7ull,
    0x22CA92B01161860Full, 0x9FC7007CCF035A68ull, 0xA0C964D9ECD580FCull,
    0x2C90F73CA03181FCull, 0x185CF84E5691EB9Eull, 0x4FC1F5EF2752AA9Bull,
    0xF5B7391A5E0A33EBull, 0xB9B84B83B4E96C9Cull, 0x5E42FE712A5CD9B4ull,
    0xA150F2F90C3F97DCull, 0x7FA522D75E2D637Dull, 0x181AD0CC0DFFD32Bull,
    0x3889ED981E854028ull, 0xFB4297E8C586EE2Dull, 0x6D064A45BB28059Cull,
    0x90563609B3EC860Cull, 0x7AA4FCE94097C666ull, 0x1326BAC06B911E08ull,
    0xB926168D2B154F34ull, 0x9919848945B1948Dull, 0xA2A98FC534825EBEull,
    0xE9809095213EF0B6ull, 0x582E5483707BC0E9ull, 0x086E9414A88A6AF5ull,
    0xEE86B98D20F6743Dull, 0xF89B7FF609B1C0A7ull, 0x4C7D9CC19E22C3E8ull,
    0x9A97005024562A6Full, 0x5DD41CF423E6EBEFull, 0xDF13609C0468E227ull,
    0x6E0DA4F64188155Aull, 0xB755BA4B50D7D4A1ull, 0x887A3484647479BDull,
    0xAB8EEBE9BF2139A0ull, 0x75542C5D4CD2A6FFull};

/*
void TestHash64(uint64_t expected, const uint8_t* data, size_t size,
                const uint64_t* key) {
  uint64_t hash = HighwayHash64(data, size, key);
  if (expected != hash) {
    printf("Test failed: expected %016"PRIx64", got %016"PRIx64", size: %d\n",
           expected, hash, (int) size);
    exit(1);
  }
}
*/

int main() {
  char fmt[30] = "%c%c%c%c%c%c%c%c%c%c\x00";
  char s[11];
  for(int i1=0x30; i1<=0x31; i1++){
    for(int i2=0x30; i2<=0x39; i2++){
      for(int i3=0x30; i3<=0x39; i3++){
        for(int i4=0x30; i4<=0x39; i4++){
          for(int i5=0x30; i5<=0x39; i5++){
            for(int i6=0x30; i6<=0x39; i6++){
              for(int i7=0x30; i7<=0x39; i7++){
                for(int i8=0x30; i8<=0x39; i8++){
                  for(int i9=0x30; i9<=0x39; i9++){
                    for(int i10=0x30; i10<=0x39; i10++){
                        snprintf(s, 11, fmt, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10);
                        //printf("%s", s);
                        // exit(0);
                        uint64_t hash = HighwayHash64(s, 10, kTestKey1);
                        if(hash==0x7CDCCF71350B7DB8ull){
                          printf("%s %p\n", s, hash);
                          printf("Test success\n");
                        }
  }
  }
  }
  }
  }
  }
  }
  }
  }
  }

  return 0;
}
