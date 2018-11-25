#include "highwayhash/c_bindings.h"
#include<stdio.h>
int calcu(){
	const uint64_t key[4] = {1, 2, 3, 4};
	char in[8] = {1};
	return HighwayHash64(key, in, 8);
}
int main(){
	printf("%x",calcu());
	return 0;
}