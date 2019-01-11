#ifndef SAGE_ENTITY_HPP
#define SAGE_ENTITY_HPP

#include "sage/dtype/dtype.hpp"
#include "sage/graph/item.hpp"
#include "sage_pch.hpp"

namespace sage {

  class SAGE_API Entity {
   private:
    item::Scope m_Scope;
    item::Type m_Type;
    item::Property m_Prop;

   public:
    Entity();
    ~Entity();
  };

}  // namespace sage
#endif  // !SAGE_ENTITY_HPP