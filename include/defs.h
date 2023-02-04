#ifndef DEFS_H
#define DEFS_H

#define DEBUG 1

#if DEBUG == 1
#define debug(x) Serial.print(x)
#define debugln(x) Serial.println(x)
#define debugf(x, y) Serial.printf(x, y)

#else

#define debug(x)
#define debugln(x)
#define debugf(x, y)

#endif

// pins
#define SERVO_PIN 25

#endif


