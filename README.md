# ideh-ctf-2021-writeups
# waht-u-have-done challenge
# solution
 The tiff image "ctf.tiff" is a scrambled/permuted image using a permutation map with 256 elements for rows and columns.
 The CTF image contains an expression written in rail_fence cipher with 4 rails saying "Paae5sFettMphL26eOeiruinlTatBtfhlmossyTe"
 This expression (when decrypted) it yeilds to "PermutationMaplsTheLast256BytesOfTheFile" which means that the CTF image is a permuted image, and must be descrambled back.
 So the last 256 bytes of the file is simply the permutation map.
 We use this map for de-scrambling rows and columns of the image, simply by mapping each row/column entry back to the entry of the key
 The final descrambled image "Solution.tiff" contains the Flag which says: IDEH{Never_Trust_Permutation_Only_Schemes}



# This are the 256 elements Key used in this chalenge as generated by Octave (1-based indexing) (in decimal notation)
 name: key
 type: matrix
 rows: 1
 columns: 256
 50 137 53 147 35 7 119 9 240 27 177 68 216 170 14 74 24 205 93 215 163 190 231 111 28 20 10 76 200 169 39 192 244 75 199 25 44 32 210 136 42 256 86 239 138 110 67 69 65 203 106 217 243 247 155 29 173 45 84 185 226 34 149 125 31 176 184 234 46 221 101 214 140 62 59 19 47 135 83 122 82 218 251 78 186 230 164 97 246 159 178 208 124 132 57 15 128 165 167 188 213 73 87 183 191 40 254 150 81 127 227 166 146 241 172 116 113 109 148 16 103 70 179 77 224 112 248 12 131 151 23 141 252 118 92 201 2 55 90 245 37 209 126 233 64 114 154 96 100 129 223 253 242 1 249 38 237 181 145 143 72 61 8 194 54 238 195 133 160 49 144 18 98 94 123 5 91 30 11 60 17 3 108 51 99 198 22 236 152 255 21 235 207 153 4 80 189 33 222 58 157 134 130 202 107 229 156 43 196 168 219 162 105 204 220 206 142 232 36 117 95 88 121 212 41 225 63 56 161 174 52 180 26 6 182 187 197 158 120 193 102 71 228 66 211 139 104 85 48 250 171 13 79 115 89 175

# for more information about the Cryptographic image Scrambling techniques
https://www.researchgate.net/publication/331064749_Cryptographic_image_Scrambling_techniques
