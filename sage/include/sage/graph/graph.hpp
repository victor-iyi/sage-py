#ifndef SAGE_GRAPH_HPP
#define SAGE_GRAPH_HPP

#include "sage_pch.hpp"

namespace sage {

  namespace graph {

    class SAGE_API Entity {
     public:
      Entity();
      ~Entity();

     private:
      std::string _m_MachineCode;
    };

    class SAGE_API Node : Entity {};

    enum Property {

    };

  }  // namespace graph

}  // namespace sage

#endif  // !SAGE_GRAPH_HPP