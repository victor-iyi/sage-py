#include "sage/dtype/dtype.hpp"

namespace sage {

  namespace dtype {

    struct Thing {
      URL url;
      URL image;
      URL sameAs;
      URL additionalType;

      Text name;
      Text description;
      Text alternateName;
      Text disambiguatingDescription;
    };

    struct Action : public Thing {};

    struct CreativeWork : public Thing {};

    struct Event : public Thing {};

    struct Intangible : public Thing {};

    struct Organization : public Thing {};

    struct Person : public Thing {};

    struct Place : public Thing {};

    struct Product : public Thing {};

  }  // namespace dtype

}  // namespace sage