#ifndef _RANDOMDGEN__XOROSHIRO128_H_
#define _RANDOMDGEN__XOROSHIRO128_H_

#include "../common/randomgen_config.h"

typedef struct XOROSHIRO128_STATE_T
{
  uint64_t s[2];
  int has_uint32;
  uint32_t uinteger;
} xoroshiro128_state_t;

static INLINE uint64_t rotl(const uint64_t x, int k)
{
  return (x << k) | (x >> (64 - k));
}

static INLINE uint64_t xoroshiro128_next(uint64_t *s)
{
  const uint64_t s0 = s[0];
  uint64_t s1 = s[1];
  const uint64_t result = s0 + s1;

  s1 ^= s0;
  s[0] = rotl(s0, 24) ^ s1 ^ (s1 << 16); // a, b
  s[1] = rotl(s1, 37);                   // c

  return result;
}

static INLINE uint64_t xoroshiro128plusplus_next(uint64_t *s) {
	const uint64_t s0 = s[0];
	uint64_t s1 = s[1];
	const uint64_t result = rotl(s0 + s1, 17) + s0;

	s1 ^= s0;
	s[0] = rotl(s0, 49) ^ s1 ^ (s1 << 21); // a, b
	s[1] = rotl(s1, 28); // c

	return result;
}

static INLINE uint64_t xoroshiro128_next64(xoroshiro128_state_t *state)
{
  return xoroshiro128_next(&state->s[0]);
}

static INLINE uint64_t xoroshiro128plusplus_next64(xoroshiro128_state_t *state)
{
  return xoroshiro128plusplus_next(&state->s[0]);
}

static INLINE uint32_t xoroshiro128_next32(xoroshiro128_state_t *state)
{
  uint64_t next;
  if (state->has_uint32)
  {
    state->has_uint32 = 0;
    return state->uinteger;
  }
  next = xoroshiro128_next(&state->s[0]);
  state->has_uint32 = 1;
  state->uinteger = (uint32_t)(next >> 32);
  return (uint32_t)(next & 0xffffffff);
}

static INLINE uint32_t xoroshiro128plusplus_next32(xoroshiro128_state_t *state)
{
  uint64_t next;
  if (state->has_uint32)
  {
    state->has_uint32 = 0;
    return state->uinteger;
  }
  next = xoroshiro128plusplus_next(&state->s[0]);
  state->has_uint32 = 1;
  state->uinteger = (uint32_t)(next >> 32);
  return (uint32_t)(next & 0xffffffff);
}

void xoroshiro128_jump(xoroshiro128_state_t *state);
void xoroshiro128plusplus_jump(xoroshiro128_state_t *state);

#endif
