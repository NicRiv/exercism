#include "reverse_string.h"

namespace reverse_string
{
    std::string reverse_string(std::string phrase)
    {
        std::string new_phrase;
        for (int i = phrase.length() - 1; i >= 0; i--)
        {
            new_phrase += phrase[i];
        }

        return new_phrase;
    }
} // namespace reverse_string